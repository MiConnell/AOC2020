def tree_counter(file: str) -> int:
    with open(file, "r") as f:
        total = 0
        lines = [line.replace("\n", "") for line in f.readlines()]
        x, y = 0, 0
        x += 3
        x %= len(lines[0])
        y += 1
        while y < len(lines):
            if lines[y][x] == "#":
                total += 1
            x += 3
            x %= len(lines[0])
            y += 1

    return total


if __name__ == "__main__":
    print(tree_counter("./blob.txt"))
