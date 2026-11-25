#Interface Parser

A small Python project that reads sample show ip interface brief output and turns each line into a dictionary using regex. Tested with Pytest.

No real network device needed.

#Example

#Input:

GigabitEthernet0/0     192.168.1.1     YES manual up                    up

#Output:

{"interface": "GigabitEthernet0/0", "ip": "192.168.1.1", "status": "up", "protocol": "up"}

#Structure
interface_parser/
    data/sample_output.txt
    parser.py
    test_parser.py
    README.md

#Setup

    python3 -m venv venv
    source venv/bin/activate
    pip install pytest

#Run

    python3 parser.py
    pytest -v

#Tests

    Counts 4 interfaces (header skipped)
    Checks exact values of the first row
    Handles administratively down and ignores junk lines