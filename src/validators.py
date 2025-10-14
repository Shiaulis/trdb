VALID_PLAYER_ID_LENGTH = 32


def validate_player_id(player_id):
    """
    Validate a player ID for TPL roster database.

    Player IDs must be valid MD5 hashes: 32-character lowercase hexadecimal strings.

    Args:
        player_id: The player ID to validate.

    Returns:
        bool: True if player_id is valid, False otherwise.
    """
    if not is_string(player_id):
        return False

    if not is_valid_length(player_id):
        return False

    if not contains_valid_characters(player_id):
        return False

    if not is_lowercased(player_id):
        return False

    return True


def is_string(player_id):
    """Check if player_id is a string."""
    return isinstance(player_id, str)


def is_valid_length(player_id):
    """Check if player_id has the correct length (32 characters)."""
    return len(player_id) == VALID_PLAYER_ID_LENGTH


def contains_valid_characters(player_id):
    """Check if player_id contains only valid hexadecimal characters (0-9, a-f)."""
    try:
        int(player_id, 16)
        return True
    except ValueError:
        return False


def is_lowercased(player_id):
    """Check if player_id is entirely lowercase."""
    return player_id.islower()
