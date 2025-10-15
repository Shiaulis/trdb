from pathlib import Path
import typer
from rich import print
from src.reader import read


def main(path: Path):
    """Validate a CSV list of player identifiers."""

    players = read(path)
    for player in players:
        player.print()


if __name__ == "__main__":
    typer.run(main)
