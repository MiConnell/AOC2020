import itertools
import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str, preamble: int) -> int:
    b = s.splitlines()
    start = 0
    while b[preamble] != b[-1]:
        checklist = [
            int(f) + int(s) for f, s in itertools.combinations(b[start:preamble], 2)
        ]
        if (goal := int(b[preamble])) not in checklist:
            return goal
        start += 1
        preamble += 1
    return 0


if __name__ == "__main__":
    print(solver(file_reader(file), 25))
