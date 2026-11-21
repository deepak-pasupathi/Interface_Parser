import re

PATTERN = re.compile(
    r"^(\S+)\s+"                              
    r"(\S+)\s+"                               
    r"\S+\s+\S+\s+"                           
    r"(up|down|administratively down)\s+"     
    r"(up|down)\s*$"                          
)



def parse_interfaces(text):
    results = []
    for line in text.splitlines():
        match = PATTERN.match(line.strip())
        if match:
            results.append({
                "interface":match.group(1),
                "ip" : match.group(2),
                "status" : match.group(3),
                "protocol" : match.group(4),
            })
    return results


def parse_file(path):
    with open(path) as f:
        return parse_interfaces(f.read())


if __name__ == "__main__":
    for row in parse_file("data/sample_output.txt"):
        print(row)


