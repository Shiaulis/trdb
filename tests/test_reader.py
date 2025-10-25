import csv
from pathlib import Path
from src.roster_reader import read_players
from src.roster_reader import PLAYER_NAME_COLUMN
from src.roster_reader import PLAYER_ID_COLUMN


def test_reader_when_opens_correct_file(tmp_path: Path):
    valid_file_path = create_valid_file(tmp_path)
    players = read_players(valid_file_path)
    assert len(players) == 2
    assert players[0].player_id == "80c05c1faa7c0948693c92fda6873edd"
    assert players[0].player_name == "Telbin"
    assert players[1].player_id == "b8610bbb3a7d30d45f4e9194c7f010d2"
    assert players[1].player_name == "Josh"


def create_valid_file(tmp_path: Path) -> Path:
    csv_file_path = tmp_path / "valid_roster.csv"
    player_name_column = PLAYER_NAME_COLUMN
    player_id_column = PLAYER_ID_COLUMN

    with open(csv_file_path, "w") as csvfile:
        field_names = [player_name_column, player_id_column]
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerow({
            player_name_column: "Telbin",
            player_id_column: "80c05c1faa7c0948693c92fda6873edd"
        })
        writer.writerow({
            player_name_column: "Josh",
            player_id_column: "b8610bbb3a7d30d45f4e9194c7f010d2"
        })

    return csv_file_path
