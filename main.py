from pathlib import Path
import typer
from src.roster_reader import read_players


def main(roster_path: Path):
    """Validate a CSV list of player identifiers."""

    players = read_players(roster_path)
    for player in players:
        player.print()


if __name__ == "__main__":
    typer.run(main)
