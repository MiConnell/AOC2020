import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def tree_counter(file: str) -> int:
    total = 0
    with open(file, "r") as f:
        trees = [line.replace("\n", "") for line in f.readlines()]
        x, y = 0, 0
        x += 3
        x %= len(trees[0])
        y += 1
        while y < len(trees):
            if trees[y][x] == "#":
                total += 1
            x += 3
            x %= len(trees[0])
            y += 1

    return total


if __name__ == "__main__":
    print(tree_counter(file))
