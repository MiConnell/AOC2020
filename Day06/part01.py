import os
from typing import List

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> List[str]:
    with open(file, "r") as f:
        return f.read().split("\n\n")


def solver(s: List[str]) -> int:
    answers = [set(a.replace("\n", "")) for a in s]
    return sum(len(ans) for ans in answers)


if __name__ == "__main__":
    print(solver(file_reader(file)))
