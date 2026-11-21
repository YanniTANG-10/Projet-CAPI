"""Interface console du walking skeleton de Planning Poker."""

import argparse
from pathlib import Path

from game import AVAILABLE_RULES, Session, load_backlog, validate_player_count, validate_players


def read_players() -> list[str]:
    while True:
        text = input("Nombre de joueurs : ").strip()
        if not text.isdigit():
            print("Saisissez un entier.")
            continue
        try:
            count = validate_player_count(int(text))
            break
        except ValueError as error:
            print(error)

    while True:
        names = [input(f"Pseudo du joueur {n} : ").strip() for n in range(1, count + 1)]
        try:
            return validate_players(names)
        except ValueError as error:
            print(f"{error} Recommencez.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Planning Poker — walking skeleton")
    parser.add_argument(
        "backlog",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parent / "exemples" / "backlog.json",
        help="Chemin du backlog JSON (facultatif).",
    )
    args = parser.parse_args()

    try:
        players = read_players()
        session = Session(
            players=players,
            backlog=load_backlog(args.backlog),
            rule=AVAILABLE_RULES[0],
        )
    except ValueError as error:
        print(f"Erreur : {error}")
        return 1
    except (EOFError, KeyboardInterrupt):
        print("\nSaisie interrompue.")
        return 1

    print("\nJoueurs : " + ", ".join(session.players))
    print(f"Règle : {session.rule.name}")
    first_feature = session.backlog[0]
    print(f"Première fonctionnalité : {first_feature['id']} — {first_feature['titre']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())