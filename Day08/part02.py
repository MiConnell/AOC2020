import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def answer_checker(file: str) -> int:
    with open(file, "r") as f:
        return 0


if __name__ == "__main__":
    print(answer_checker(file))
