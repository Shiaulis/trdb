VALID_PLAYER_ID_LENGTH = 32


def validate_player_id(player_id):
    if not is_string(player_id):
        return False

    if not is_valid_length(player_id):
        return False

    if not is_contain_valid_characters(player_id):
        return False

    if not is_lowercased(player_id):
        return False

    return True


def is_string(player_id):
    return isinstance(player_id, str)


def is_valid_length(player_id):
    return len(player_id) == VALID_PLAYER_ID_LENGTH


def is_contain_valid_characters(player_id):
    return player_id.isalnum()


def is_lowercased(player_id):
    return player_id.islower()
