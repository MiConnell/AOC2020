import os
from typing import List

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    super_set = set()
    adapters = sorted([int(n) for n in s.splitlines()])
    goal = adapters[-1]
    lst: List[List[int]] = []
    while sum(lst) == goal:
        super_set.add(lst)
    return 0


if __name__ == "__main__":
    print(solver(file_reader(file)))
