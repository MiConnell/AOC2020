import os
import re
from typing import Dict
from typing import List
from typing import Tuple


file = os.path.join(os.path.dirname(__file__), "blob.txt")

PARENT = re.compile(r"^(\w+ \w+) bags contain (.+)$")
CHILD = re.compile(r"(\d+) (\w+ \w+)")
goal_bag = "shiny gold"


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


def solver(s: Dict[str, List[Tuple[int, str]]]) -> int:
    total = 0
    options = [(1, goal_bag)]

    while options:
        n, bag = options.pop()
        total += n

        for child_n, child in s[bag]:
            options.append((n * child_n, child))

    total -= 1
    return total


if __name__ == "__main__":
    print(solver(build_dictionary(file_reader(file))))
