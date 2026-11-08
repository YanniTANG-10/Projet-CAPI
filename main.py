"""Interface console du walking skeleton de Planning Poker."""

import argparse
from pathlib import Path

from game import Session, load_backlog


def read_players() -> list[str]:
    while True:
        try:
            count = int(input("Nombre de joueurs : "))
            if count > 1:
                break
        except ValueError:
            pass
        print("Saisissez un entier supérieur à 1.")

    players = []
    for number in range(1, count + 1):
        nickname = input(f"Pseudo du joueur {number} : ").strip()
        while not nickname:
            print("Le pseudo ne peut pas être vide.")
            nickname = input(f"Pseudo du joueur {number} : ").strip()
        players.append(nickname)
    return players


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
        session = Session(players=players, backlog=load_backlog(args.backlog))
    except ValueError as error:
        print(f"Erreur : {error}")
        return 1
    except (EOFError, KeyboardInterrupt):
        print("\nSaisie interrompue.")
        return 1

    print("\nJoueurs : " + ", ".join(session.players))
    first_feature = session.backlog[0]
    print(f"Première fonctionnalité : {first_feature['id']} — {first_feature['titre']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
