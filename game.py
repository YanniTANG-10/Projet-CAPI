"""Données de la session et chargement du backlog, sans interface."""

import json
from dataclasses import dataclass
from pathlib import Path
minimumOfPlayers = 2
class ValidationRule:
    """Règle qui décide si les votes d'un tour valident l'estimation."""

    name = "Règle"

    def is_validated(self, votes: list, round_number: int = 1):
        """Renvoie l'estimation retenue, ou None si le tour n'est pas validé."""
        raise NotImplementedError


class StrictRule(ValidationRule):
    name = "Unanimité (stricte)"

    def is_validated(self, votes: list, round_number: int = 1):
        if not votes:
            raise ValueError("Votes non trouvables")
        else: 
            differents = False
            for vote in votes:
                if vote != votes[0]:
                    differents =True
                    return None
            if not differents: return votes[0]
                
                


class MedianRule(ValidationRule):
    name = "Médiane"

    def is_validated(self, votes: list, round_number: int = 1):
        raise NotImplementedError  # plus tard


AVAILABLE_RULES = [StrictRule(), MedianRule()]


def get_rule(name: str) -> ValidationRule:
    for rule in AVAILABLE_RULES:
        if rule.name == name:
            return rule
    raise ValueError(f"Règle inconnue : {name}")
@dataclass
class Session:
    players: list[str]
    backlog: list[dict[str, str]]
    rule: ValidationRule

def validate_player_count(count: int) -> int:
    if count < minimumOfPlayers:
        raise ValueError(f"Un minimum de {minimumOfPlayers} joueurs est requis.")
    return count


def validate_players(players: list[str]) -> list[str]:
    """Vérifie le nombre, les pseudos vides et les doublons."""
    validate_player_count(len(players))
    cleaned = [name.strip() for name in players]
    if any(not name for name in cleaned):
        raise ValueError("Le pseudo ne peut pas être vide.")
    if len({name.lower() for name in cleaned}) != len(cleaned):
        raise ValueError("Les pseudos doivent être uniques.")
    return cleaned



def load_backlog(path: Path) -> list[dict[str, str]]:
    """Charge les fonctionnalités et vérifie leur structure."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"Fichier introuvable : {path.name}. Vérifiez le nom ou sélectionnez un fichier existant.") from error
    except IsADirectoryError as error:
        raise ValueError("Le chemin désigne un dossier. Sélectionnez un fichier JSON.") from error
    except PermissionError as error:
        raise ValueError("Accès refusé. Choisissez un fichier que vous pouvez lire.") from error
    except OSError as error:
        raise ValueError("Impossible de lire ce fichier. Vérifiez qu’il est accessible.") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"JSON invalide à la ligne {error.lineno}, colonne {error.colno}. Vérifiez le contenu du fichier.") from error
    except UnicodeError as error:
        raise ValueError("Encodage invalide. Enregistrez le fichier en UTF-8.") from error

    if not isinstance(data, dict):
        raise ValueError("Le backlog doit être un objet JSON.")
    features = data.get("fonctionnalites")
    if not isinstance(features, list):
        raise ValueError("Le champ 'fonctionnalites' doit être une liste JSON.")
    if not features:
        raise ValueError("Le backlog est vide. Ajoutez au moins une fonctionnalité.")

    for feature in features:
        if not isinstance(feature, dict):
            raise ValueError("Chaque fonctionnalité doit être un objet JSON.")
        for field in ("id", "titre"):
            if not isinstance(feature.get(field), str) or not feature[field].strip():
                raise ValueError(f"Chaque fonctionnalité doit avoir un '{field}' non vide.")
    return features
