import os
import re
from collections import defaultdict
from typing import DefaultDict
from typing import List

file = os.path.join(os.path.dirname(__file__), "blob.txt")

PARENT = re.compile(r"^(\w+ \w+) bags contain (.+)$")
CHILD = re.compile(r"(\d+) (\w+ \w+)")

GOAL_BAG = "shiny gold"


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def build_dictionary(s: str) -> DefaultDict[str, List[str]]:
    parents: DefaultDict[str, List[str]] = defaultdict(list)
    for line in s.splitlines():
        line_match = PARENT.match(line)
        assert line_match, line
        parent = line_match[1]
        children = line_match[2]

        for _, child in CHILD.findall(children):
            parents[child].append(parent)

    return parents


def solver(s: DefaultDict[str, List[str]]) -> int:
    seen = set()
    options = [GOAL_BAG]

    while options:
        bag = options.pop()
        seen.add(bag)
        options.extend(s[bag])

    return len(seen - {GOAL_BAG})


if __name__ == "__main__":
    print(solver(build_dictionary(file_reader(file))))


"""
light red bag    | [bright white bag, muted yellow bag]  x
dark orange bag  | [bright white bag, muted yellow bag]  x
bright white bag | [shiny gold bag]                      x
muted yellow bag | [shiny gold bag, faded blue bag]      x
shiny gold bag   | [dark olive bag, vibrant plum bag]
dark olive bag   | [faded blue bag, dotted black bag]
vibrant plum bag | [faded blue bag, dotted black bag]
faded blue bag   | [no other bag]
dotted black bag | [no other bag]
"""
