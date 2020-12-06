from typing import Set

COUNTLETTERS = {"a", "b", "c", "x", "y", "z"}


def counter(s: Set[str]) -> int:
    return len(s)


def answer_checker(file: str) -> int:
    total = 0
    with open(file, "r") as f:
        answers = [set(a.replace("\n", "")) for a in f.read().strip().split("\n\n")]
        for ans in answers:
            total += counter(ans)
    return total


if __name__ == "__main__":
    print(answer_checker("./blob.txt"))
