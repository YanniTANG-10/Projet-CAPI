"""Données de la session et chargement du backlog, sans interface."""

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Session:
    players: list[str]
    backlog: list[dict[str, str]]


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
