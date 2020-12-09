import itertools
import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def _solver(blob: str, preamble: int) -> int:
    b = blob.splitlines()
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


def solver(blob: str) -> int:
    b = [int(b) for b in blob.splitlines()]
    start = 0
    end = 0
    goal = _solver(file_reader(file), 25)
    current = b[0]
    while True:
        if current < goal:
            end += 1
            current += b[end]
        elif current > goal:
            current -= b[start]
            start += 1
        else:
            lst = b[start : end + 1]
            return min(lst) + max(lst)


if __name__ == "__main__":
    print(solver(file_reader(file)))
