import csv
from pathlib import Path
from src.models import Player

PLAYER_NAME_COLUMN = "player_name"
PLAYER_ID_COLUMN = "player_id"


def read_players(path: Path) -> list:
    players = []
    with path.open() as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_name = row[PLAYER_NAME_COLUMN]
            player_id = row[PLAYER_ID_COLUMN]
            player = Player(player_name, player_id)
            players.append(player)

    return players
