from rich import print
from rich.text import Text


class Player:
    """ Represents a player with their properties."""

    def __init__(self, player_name: str, player_id: str):
        self.player_name = player_name
        self.player_id = player_id

    def print(self):
        text = Text()
        text.append("Player: ", style="bold cyan")
        text.append(self.player_name)
        text.append("ID: ", style="dim")
        text.append(self.player_id)
        print(text)
