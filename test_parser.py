from pathlib import Path
from parser import parse_interfaces, parse_file


DATA_FILE = Path(__file__).parent / "data" / "sample_output.txt"


def test_parses_all_interfaces():
    rows = parse_file(DATA_FILE)
    assert len(rows) == 4


def test_first_interface_values():
    rows = parse_file(DATA_FILE)
    assert rows[0] == {
        "interface" : "GigabitEthernet0/0",
        "ip": "192.168.1.1",
        "status": "up",
        "protocol": "up",
    }


def test_adminstratively_down_and_junk_line():
    text = (
        "this line is garbage\n"
        "GigabitEthernet0/1 unassigned YES unset administratively down down\n"

    )
    rows = parse_interfaces(text)
    assert len(rows) == 1
    assert rows[0]["status"] == "administratively down"
    assert rows[0]["protocol"] == "down"