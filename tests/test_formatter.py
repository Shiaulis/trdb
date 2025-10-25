from src.roster_formatter import format_report
from src.models import ValidationReport


def test_successfully_formatted_message():
    players_count = 100
    successful_report = ValidationReport(players_count, [])
    sut = format_report(successful_report)

    assert f"**{players_count}**" in sut
    assert "ROSTER VALIDATION COMPLETE" in sut
    assert "ready to submit" in sut
    assert "Invalid Player identifiers" not in sut
