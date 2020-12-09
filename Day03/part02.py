import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(s: str) -> str:
    with open(s, "r") as f:
        return f.read()


def _solver(s: str, x_shift: int, y_shift: int) -> int:
    total = 0
    x, y = 0, 0
    x += x_shift
    x %= len((trees := s.splitlines())[0])
    y += y_shift
    while y < len(trees):
        if trees[y][x] == "#":
            total += 1
        x += x_shift
        x %= len(trees[0])
        y += y_shift

    return total


def solver(s: str) -> int:
    return (
        _solver(s, 1, 1)
        * _solver(s, 3, 1)
        * _solver(s, 5, 1)
        * _solver(s, 7, 1)
        * _solver(s, 1, 2)
    )


if __name__ == "__main__":
    print(solver(file_reader(file)))

"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""
