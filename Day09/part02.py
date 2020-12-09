import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")

INVALID = 1721308972


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(blob: str) -> int:
    b = [int(b) for b in blob.splitlines()]
    start = 0
    end = 0
    goal = INVALID
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
