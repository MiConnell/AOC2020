import os
from typing import List

file = os.path.join(os.path.dirname(__file__), "blob.txt")

REQUIRED = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}


def file_reader(file: str) -> List[str]:
    with open(file, "r") as f:
        return f.read().split("\n\n")


def solver(s: List[str]) -> int:
    total = 0
    for p in s:
        p = p.replace("\n", " ")
        check = [a.split(":")[0] for a in p.split(" ")]
        if "cid" in check:
            check.remove("cid")
        if len(check) > 6:
            total += 1
    return total


if __name__ == "__main__":
    print(solver(file_reader(file)))
