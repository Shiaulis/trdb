class Player:
    """ Represents a player with their properties."""

    def __init__(self, player_name: str, player_id: str):
        self.player_name = player_name
        self.player_id = player_id


class ValidationReport:
    """Represents result of player list validation"""

    def __init__(self, total_count: int, invalid_players: list[Player]):
        self.total_count = total_count
        self.invalid_players = invalid_players

    @property
    def invalid_count(self) -> int:
        return len(self.invalid_players)

    @property
    def valid_count(self) -> int:
        return self.total_count - self.invalid_count
