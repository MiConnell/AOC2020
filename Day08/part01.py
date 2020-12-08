import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")
# file = "./tests/test_blob.txt"


def solver(file: str) -> int:
    with open(file, "r") as f:
        for line in f.readlines():
            line
    return 0


if __name__ == "__main__":
    print(solver(file))
