"""Interface graphique du walking skeleton de Planning Poker."""

import tkinter as tk
from pathlib import Path
from tkinter import filedialog, ttk
from tkinter import font as tkfont

from game import (
    AVAILABLE_RULES,
    Session,
    get_rule,
    load_backlog,
    validate_player_count,
    validate_players,
)

# Palette : uniquement du visuel, aucune logique ne dépend de ces valeurs.
BG = "#f3f4f8"
CARD = "#ffffff"
TEXT = "#1f2937"
MUTED = "#6b7280"
ACCENT = "#4f46e5"
ACCENT_HOVER = "#4338ca"
ACCENT_PRESSED = "#3730a3"
BORDER = "#d9dce6"
ERROR = "#b91c1c"
SUCCESS = "#15803d"


class PlanningPokerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.session = None
        root.title("Planning Poker")
        root.geometry("760x820")
        root.minsize(620, 700)
        root.configure(bg=BG)
        self.font_family = tkfont.nametofont("TkDefaultFont").actual("family")
        self.apply_theme()

        self.player_count = tk.StringVar(value="2")
        self.rule_name = tk.StringVar(value=AVAILABLE_RULES[0].name)
        self.backlog_path = tk.StringVar(
            value=str(Path(__file__).resolve().parent / "exemples" / "backlog.json")
        )
        self.status = tk.StringVar(value="Préparez votre session pour commencer.")
        self.players_summary = tk.StringVar()

        content = ttk.Frame(root, padding=28, style="App.TFrame")
        content.pack(fill="both", expand=True)
        content.columnconfigure(0, weight=1)
        ttk.Label(content, text="Planning Poker", style="Title.TLabel").grid(
            row=0, column=0, sticky="w"
        )
        ttk.Label(
            content,
            text="Créez une session et découvrez le backlog.",
            style="Subtitle.TLabel",
        ).grid(row=1, column=0, sticky="w", pady=(4, 22))

        players = ttk.LabelFrame(
            content, text="1. Joueurs", padding=18, style="Card.TLabelframe"
        )
        players.grid(row=2, column=0, sticky="ew")
        players.columnconfigure(1, weight=1)
        ttk.Label(players, text="Nombre de joueurs", style="Card.TLabel").grid(
            row=0, column=0, sticky="w"
        )
        ttk.Entry(
            players, textvariable=self.player_count, width=8, justify="center"
        ).grid(row=0, column=1, sticky="w", padx=12)
        ttk.Label(
            players, text="Pseudos — un joueur par ligne", style="CardMuted.TLabel"
        ).grid(row=1, column=0, columnspan=2, sticky="w", pady=(16, 6))
        self.nicknames = tk.Text(
            players,
            height=5,
            font=(self.font_family, 13),
            wrap="word",
            bg=CARD,
            fg=TEXT,
            insertbackground=TEXT,
            selectbackground="#c7d2fe",
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER,
            highlightcolor=ACCENT,
            padx=10,
            pady=8,
        )
        self.nicknames.grid(row=2, column=0, columnspan=2, sticky="ew")

        rule = ttk.LabelFrame(
            content, text="2. Règle de validation", padding=18, style="Card.TLabelframe"
        )
        rule.grid(row=3, column=0, sticky="ew", pady=(16, 0))
        rule.columnconfigure(0, weight=1)
        ttk.Combobox(
            rule,
            textvariable=self.rule_name,
            values=[r.name for r in AVAILABLE_RULES],
            state="readonly",
        ).grid(row=0, column=0, sticky="ew")

        backlog = ttk.LabelFrame(
            content, text="3. Backlog JSON", padding=18, style="Card.TLabelframe"
        )
        backlog.grid(row=4, column=0, sticky="ew", pady=16)
        backlog.columnconfigure(0, weight=1)
        ttk.Entry(backlog, textvariable=self.backlog_path).grid(
            row=0, column=0, sticky="ew"
        )
        ttk.Button(
            backlog,
            text="Parcourir…",
            command=self.choose_backlog,
            style="Secondary.TButton",
        ).grid(row=0, column=1, padx=(10, 0))
        ttk.Button(
            content,
            text="Démarrer la session",
            command=self.start_session,
            style="Accent.TButton",
        ).grid(row=5, column=0, sticky="ew")
        self.status_label = ttk.Label(
            content, textvariable=self.status, wraplength=550, style="Status.TLabel"
        )
        self.status_label.grid(row=6, column=0, sticky="w", pady=12)
        self.status.trace_add("write", self.update_status_color)

        result = ttk.LabelFrame(
            content, text="Session", padding=18, style="Card.TLabelframe"
        )
        result.grid(row=7, column=0, sticky="nsew")
        content.rowconfigure(7, weight=1)
        result.columnconfigure(0, weight=1)
        ttk.Label(
            result,
            textvariable=self.players_summary,
            wraplength=530,
            style="CardBold.TLabel",
        ).grid(row=0, column=0, sticky="w")
        self.feature = tk.Text(
            result,
            height=5,
            font=(self.font_family, 14),
            wrap="word",
            state="disabled",
            bg="#f9fafb",
            fg=TEXT,
            selectbackground="#c7d2fe",
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER,
            padx=12,
            pady=10,
            spacing3=6,
        )
        self.feature.grid(row=1, column=0, sticky="nsew", pady=(10, 0))
        scrollbar = ttk.Scrollbar(result, orient="vertical", command=self.feature.yview)
        scrollbar.grid(row=1, column=1, sticky="ns", pady=(10, 0))
        self.feature.configure(yscrollcommand=scrollbar.set)
        result.rowconfigure(1, weight=1)
        self.show_feature("Les fonctionnalités du backlog apparaîtront ici.")

    def apply_theme(self):
        """Thème visuel de la fenêtre (couleurs, polices, boutons)."""
        style = ttk.Style(self.root)
        style.theme_use("clam")
        fam = self.font_family
        self.root.option_add("*TCombobox*Listbox.font", (fam, 11))
        style.configure(".", font=(fam, 11), background=BG, foreground=TEXT)
        style.configure("App.TFrame", background=BG)
        style.configure("Title.TLabel", background=BG, foreground=TEXT, font=(fam, 26, "bold"))
        style.configure("Subtitle.TLabel", background=BG, foreground=MUTED, font=(fam, 12))
        style.configure("Status.TLabel", background=BG, foreground=MUTED, font=(fam, 11))
        style.configure(
            "Card.TLabelframe", background=CARD, bordercolor=BORDER, borderwidth=1, relief="solid"
        )
        style.configure(
            "Card.TLabelframe.Label", background=CARD, foreground=ACCENT, font=(fam, 11, "bold")
        )
        style.configure("Card.TLabel", background=CARD, foreground=TEXT)
        style.configure("CardMuted.TLabel", background=CARD, foreground=MUTED)
        style.configure("CardBold.TLabel", background=CARD, foreground=TEXT, font=(fam, 11, "bold"))
        style.configure(
            "TEntry", fieldbackground=CARD, bordercolor=BORDER, lightcolor=BORDER,
            darkcolor=BORDER, padding=6,
        )
        style.map(
            "TEntry",
            bordercolor=[("focus", ACCENT)],
            lightcolor=[("focus", ACCENT)],
            darkcolor=[("focus", ACCENT)],
        )
        style.configure(
            "TCombobox", fieldbackground=CARD, background=CARD, bordercolor=BORDER,
            arrowcolor=ACCENT, padding=6,
        )
        style.map(
            "TCombobox",
            fieldbackground=[("readonly", CARD)],
            selectbackground=[("readonly", CARD)],
            selectforeground=[("readonly", TEXT)],
            bordercolor=[("focus", ACCENT)],
        )
        style.configure(
            "Accent.TButton", background=ACCENT, foreground="#ffffff", font=(fam, 12, "bold"),
            padding=(16, 11), borderwidth=0, focusthickness=0, focuscolor=ACCENT,
        )
        style.map(
            "Accent.TButton",
            background=[("pressed", ACCENT_PRESSED), ("active", ACCENT_HOVER)],
            foreground=[("disabled", "#e5e7eb")],
        )
        style.configure(
            "Secondary.TButton", background="#eef0f7", foreground=TEXT, padding=(12, 7),
            bordercolor=BORDER, borderwidth=1, focusthickness=0,
        )
        style.map(
            "Secondary.TButton",
            background=[("pressed", "#dfe3f0"), ("active", "#e6e9f4")],
        )

    def update_status_color(self, *_):
        """Colore le message d'état : rouge pour une erreur, vert pour un succès."""
        text = self.status.get()
        if text.startswith(("Erreur", "Saisissez", "Choisissez")):
            color = ERROR
        elif text.startswith("Session prête"):
            color = SUCCESS
        else:
            color = MUTED
        self.status_label.configure(foreground=color)

    def show_feature(self, text: str):
        self.feature.configure(state="normal")
        self.feature.delete("1.0", "end")
        self.feature.insert("1.0", text)
        self.feature.yview_moveto(0)
        self.feature.configure(state="disabled")

    def choose_backlog(self):
        path = filedialog.askopenfilename(
            parent=self.root,
            title="Choisir un backlog",
            filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*")],
        )
        if path:
            self.backlog_path.set(path)

    def start_session(self):
        self.session = None
        self.players_summary.set("")
        self.show_feature("Les fonctionnalités du backlog apparaîtront ici.")

        try:
            count = int(self.player_count.get())
        except ValueError:
            self.status.set("Saisissez un nombre entier de joueurs.")
            return

        try:
            validate_player_count(count)
            names = [line.strip() for line in self.nicknames.get("1.0", "end-1c").splitlines()]
            if len(names) != count:
                self.status.set(f"Saisissez exactement {count} pseudos, un par ligne.")
                return
            players = validate_players(names)
        except ValueError as error:
            self.status.set(f"Erreur : {error}")
            return

        if not self.backlog_path.get().strip():
            self.status.set("Choisissez un fichier JSON.")
            return
        try:
            backlog = load_backlog(Path(self.backlog_path.get()).expanduser())
            rule = get_rule(self.rule_name.get())
        except ValueError as error:
            self.status.set(f"Erreur : {error}")
            return

        self.session = Session(players=players, backlog=backlog, rule=rule)
        self.players_summary.set(f"Joueurs : {', '.join(players)} · Règle : {rule.name}")
        self.show_feature("\n\n".join(f"{feature['id']} — {feature['titre']}" for feature in backlog))
        self.status.set(f"Session prête · {len(players)} joueurs · {len(backlog)} fonctionnalités")


def main():
    root = tk.Tk()
    PlanningPokerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()