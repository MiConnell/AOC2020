import os
from typing import Dict

file = os.path.join(os.path.dirname(__file__), "blob.txt")

directions: Dict[str, int] = {"N": 0, "E": 0, "S": 0, "W": 0}


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    for line in s.splitlines():
        ...
    return 0


if __name__ == "__main__":
    print(solver(file_reader(file)))
