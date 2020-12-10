import os
import re
from collections import defaultdict
from typing import Dict
from typing import List
from typing import Tuple


file = os.path.join(os.path.dirname(__file__), "blob.txt")

PARENT = re.compile(r"^(\w+ \w+) bags contain (.+)$")
CHILD = re.compile(r"^(\d+) (\w+ \w+)")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def build_dictionary(s: str) -> Dict[str, List[Tuple[int, str]]]:
    options = {}
    for line in s.splitlines():
        line_match = PARENT.match(line)
        assert line_match, line
        parent = line_match[1]
        children = line_match[2]

        kiddos = [(int(n), child) for n, child in CHILD.findall(children)]
        options[parent] = kiddos

    return options


def solver(s: str) -> int:
    for line in s.splitlines():
        ...
    return 0


if __name__ == "__main__":
    print(solver(file_reader(file)))
