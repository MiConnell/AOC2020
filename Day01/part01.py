import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str, goal: int) -> int:
    nums = [int(line) for line in s.splitlines()]
    for n in nums:
        if goal - n in nums:
            return (goal - n) * n
    return 0


if __name__ == "__main__":
    print(solver(file_reader(file), 2020))
