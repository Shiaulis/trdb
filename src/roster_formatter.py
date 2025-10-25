from src.models import Player, ValidationReport


def format_report(report: ValidationReport) -> str:
    if report.invalid_count == 0:
        return format_success_report(report.total_count)
    else:
        return format_failed_report(
            total_count=report.total_count,
            valid_count=report.valid_count,
            invalid_count=report.invalid_count,
            players=report.invalid_players
        )


def format_success_report(total_count: int) -> str:
    return f"""
    ✅ **ROSTER VALIDATION COMPLETE**
    All **{total_count}** player identifiers are valid!
    Your roster is ready to submit.
    """


def format_failed_report(total_count: int, valid_count: int, invalid_count: int, players: list[Player]) -> str:
    message = f"""
    📊 **ROSTER VALIDATION REPORT**

    📝 Total players: {total_count}
    ✅ Valid: {valid_count}
    ❌ Invalid: {invalid_count}

    **Invalid Player identifiers:**

    """

    for player in players:
        message += f"❌ `{player.player_id}` – {player.player_name}\n"

    message += "\n⚠️ Please fix these identifiers before submitting your roster."

    return message
