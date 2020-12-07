import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def _counter(file: str, x_shift: int, y_shift: int) -> int:
    with open(file, "r") as f:
        total = 0
        lines = [line.replace("\n", "") for line in f.readlines()]
        x, y = 0, 0
        x += x_shift
        x %= len(lines[0])
        y += y_shift
        while y < len(lines):
            if lines[y][x] == "#":
                total += 1
            x += x_shift
            x %= len(lines[0])
            y += y_shift

    return total


def tree_counter(file: str) -> int:
    return (
        _counter(file, 1, 1)
        * _counter(file, 3, 1)
        * _counter(file, 5, 1)
        * _counter(file, 7, 1)
        * _counter(file, 1, 2)
    )


if __name__ == "__main__":
    print(tree_counter(file))

"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""
