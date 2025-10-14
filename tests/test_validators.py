from src.validators import validate_player_id


def test_validate_player_id_with_none():
    """Should return False when player_id is None (wrong type)."""
    assert validate_player_id(None) is False


def test_validate_player_id_with_short_string():
    """Should return False when string has insufficient length."""
    short_string = "Short string"
    assert validate_player_id(short_string) is False


def test_validate_player_id_with_valid_string():
    """Should return True when player_id is a valid MD5 hash."""
    valid_string = "d33fe4ac81338c97290d2acd810c15e3"
    assert validate_player_id(valid_string) is True


def test_validate_player_id_with_uppercase_string():
    """Should return False when string contains uppercase letters."""
    uppercase_player_id = "D33FE4AC81338C97290D2ACD810C15E3"
    assert validate_player_id(uppercase_player_id) is False


def test_validate_player_id_with_invalid_characters():
    """Should return False when player_id contains invalid characters."""
    almost_valid_string = "d33fe4ac81338c97290d2acd810c15e!"
    assert validate_player_id(almost_valid_string) is False


def test_validate_player_id_with_non_hexadecimal_characters():
    """Should return False when player_id contains characters outside of hexadecimal range."""
    almost_valid_string = "c327bfd7c2c58f2485e58903df38s473"
    assert validate_player_id(almost_valid_string) is False
