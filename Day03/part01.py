import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    total = 0
    x, y = 0, 0
    x += 3
    x %= len((trees := s.splitlines())[0])
    y += 1
    while y < len(trees):
        if trees[y][x] == "#":
            total += 1
        x += 3
        x %= len(trees[0])
        y += 1

    return total


if __name__ == "__main__":
    print(solver(file_reader(file)))
