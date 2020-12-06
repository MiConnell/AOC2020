from typing import Any
from typing import List


def counter(lst: List[Any]) -> int:
    total = [(let, lst[0].count(let)) for let in lst[0] if lst[0].count(let) == lst[1]]
    return len(set(total))


def answer_checker(file: str) -> int:
    with open(file, "r") as f:
        answers = [
            [a.replace("\n", ""), len(a.split("\n"))]
            for a in f.read().strip().split("\n\n")
        ]
        total = sum(counter(ans) for ans in answers)
    return total


if __name__ == "__main__":
    print(answer_checker("./blob.txt"))
