import os
from typing import List

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    count = 0
    return count


if __name__ == "__main__":
    print(solver(file_reader(file)))
