import typer
from rich import print
from src.validators import validate_player_id


def main(player_id: str):
    """Validate a player ID."""

    if validate_player_id(player_id):
        print("[green]✓ Valid player identifier[/green]")
        raise typer.Exit(code=0)
    else:
        print("[red]✗ Invalid player identifier[/red]")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    typer.run(main)
