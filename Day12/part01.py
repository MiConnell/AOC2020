import os
from typing import Dict
from typing import List
from typing import Tuple

file = os.path.join(os.path.dirname(__file__), "blob.txt")

directions: Dict[str, int] = {"N": 0, "E": 0, "S": 0, "W": 0}


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def change_heading(d: str, c: str, a: int) -> str:
    opts = ["N", "E", "S", "W"]
    if c == "L":
        return opts[opts.index(d) - a % len(opts)]
    elif c == "R":
        return opts[opts.index(d) + a % len(opts)]
    else:
        raise NotImplementedError(d)


def check_opposites(d: str):
    opps = {"N": "S", "E": "W", "S": "N", "W": "E"}
    return opps[d]


def solver(s: str) -> int:
    heading: str = "E"
    for line in s.splitlines():
        dir = line[0]
        val = int(line[1:])
        if dir == "F":
            directions[heading] += val
            if directions[check_opposites(heading)] != 0:
                directions[check_opposites(heading)] -= val
        elif dir in ["R", "L"]:
            amount = val % 90
            heading = change_heading(heading, dir, amount)
        else:
            directions[dir] += val
    return (abs(directions["N"] - directions["S"])) + (
        abs(directions["E"] - directions["W"])
    )


if __name__ == "__main__":
    print(solver(file_reader(file)))


"""
F 10

E
{'N': 0, 'E': 10, 'S': 0, 'W': 0}
----------------------------------
N 3

E
{'N': 3, 'E': 10, 'S': 0, 'W': 0}
----------------------------------
F 7

E
{'N': 3, 'E': 17, 'S': 0, 'W': 0}
----------------------------------
R 90

S
{'N': 3, 'E': 17, 'S': 0, 'W': 0}
----------------------------------
F 11

S
{'N': 0, 'E': 17, 'S': 8, 'W': 0}
----------------------------------
"""
