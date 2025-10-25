from pathlib import Path
import typer
from src.roster_reader import read_players
from src.roster_validator import validate_players
from src.roster_formatter import format_report


def main(roster_path: Path):
    """Validate a CSV list of player identifiers."""

    players = read_players(roster_path)
    report = validate_players(players)
    message = format_report(report)

    print(message)


if __name__ == "__main__":
    typer.run(main)
