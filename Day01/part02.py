import itertools
import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str, goal: int) -> int:
    nums = sorted([int(line) for line in s.splitlines()], reverse=True)
    for a, b, c in itertools.combinations(nums, 3):
        if a + b + c == goal:
            return a * b * c
    return 0


if __name__ == "__main__":
    print(solver(file_reader(file), 2020))
