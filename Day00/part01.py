import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(blob: str) -> int:
    for b in blob.splitlines():
        ...
    return 0


if __name__ == "__main__":
    print(solver(file_reader(file)))
