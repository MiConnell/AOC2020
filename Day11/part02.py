import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    st = [int(i) for i in s.splitlines()]
    h = [max(st) % 3 == i for i in range(3)]
    for x in reversed(range(1, max(st) + 3)):
        h[x % 3] = sum(h) if x in st else 0  # type: ignore
    return sum(h)


if __name__ == "__main__":
    print(solver(file_reader(file)))
