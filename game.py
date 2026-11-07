"""Données de la session et chargement du backlog, sans interface."""

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Session:
    players: list[str]

