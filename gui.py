"""Interface graphique du walking skeleton de Planning Poker."""

import tkinter as tk
from pathlib import Path
from tkinter import filedialog, ttk

from game import (
    AVAILABLE_RULES,
    Session,
    get_rule,
    load_backlog,
    validate_player_count,
    validate_players,
)


class PlanningPokerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.session = None
        root.title("Planning Poker")
        root.geometry("760x820")
        root.minsize(620, 700)

        self.player_count = tk.StringVar(value="2")
        self.rule_name = tk.StringVar(value=AVAILABLE_RULES[0].name)
        self.backlog_path = tk.StringVar(
            value=str(Path(__file__).resolve().parent / "exemples" / "backlog.json")
        )
        self.status = tk.StringVar(value="Préparez votre session pour commencer.")
        self.players_summary = tk.StringVar()

        content = ttk.Frame(root, padding=24)
        content.pack(fill="both", expand=True)
        content.columnconfigure(0, weight=1)
        ttk.Label(content, text="Planning Poker", font=("Helvetica", 26, "bold")).grid(
            row=0, column=0, sticky="w"
        )
        ttk.Label(content, text="Créez une session et découvrez le backlog.").grid(
            row=1, column=0, sticky="w", pady=(4, 20)
        )

        players = ttk.LabelFrame(content, text="1. Joueurs", padding=16)
        players.grid(row=2, column=0, sticky="ew")
        players.columnconfigure(1, weight=1)
        ttk.Label(players, text="Nombre de joueurs").grid(row=0, column=0, sticky="w")
        ttk.Entry(players, textvariable=self.player_count, width=8).grid(
            row=0, column=1, sticky="w", padx=12
        )
        ttk.Label(players, text="Pseudos — un joueur par ligne").grid(
            row=1, column=0, columnspan=2, sticky="w", pady=(16, 6)
        )
        self.nicknames = tk.Text(players, height=5, font=("Helvetica", 14), wrap="word")
        self.nicknames.grid(row=2, column=0, columnspan=2, sticky="ew")

        rule = ttk.LabelFrame(content, text="2. Règle de validation", padding=16)
        rule.grid(row=3, column=0, sticky="ew", pady=(16, 0))
        rule.columnconfigure(0, weight=1)
        ttk.Combobox(
            rule,
            textvariable=self.rule_name,
            values=[r.name for r in AVAILABLE_RULES],
            state="readonly",
        ).grid(row=0, column=0, sticky="ew")

        backlog = ttk.LabelFrame(content, text="3. Backlog JSON", padding=16)
        backlog.grid(row=4, column=0, sticky="ew", pady=16)
        backlog.columnconfigure(0, weight=1)
        ttk.Entry(backlog, textvariable=self.backlog_path).grid(row=0, column=0, sticky="ew")
        ttk.Button(backlog, text="Parcourir…", command=self.choose_backlog).grid(
            row=0, column=1, padx=(10, 0)
        )
        ttk.Button(content, text="Démarrer la session", command=self.start_session).grid(
            row=5, column=0, sticky="ew"
        )
        ttk.Label(content, textvariable=self.status, wraplength=550).grid(
            row=6, column=0, sticky="w", pady=12
        )

        result = ttk.LabelFrame(content, text="Session", padding=16)
        result.grid(row=7, column=0, sticky="nsew")
        content.rowconfigure(7, weight=1)
        result.columnconfigure(0, weight=1)
        ttk.Label(result, textvariable=self.players_summary, wraplength=530).grid(
            row=0, column=0, sticky="w"
        )
        self.feature = tk.Text(
            result, height=5, font=("Helvetica", 16), wrap="word", state="disabled"
        )
        self.feature.grid(row=1, column=0, sticky="nsew", pady=(10, 0))
        scrollbar = ttk.Scrollbar(result, orient="vertical", command=self.feature.yview)
        scrollbar.grid(row=1, column=1, sticky="ns", pady=(10, 0))
        self.feature.configure(yscrollcommand=scrollbar.set)
        result.rowconfigure(1, weight=1)
        self.show_feature("Les fonctionnalités du backlog apparaîtront ici.")

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