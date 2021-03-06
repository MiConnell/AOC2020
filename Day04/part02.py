import os
import re
from typing import Dict
from typing import List
from typing import Match
from typing import Union

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


"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


def file_reader(file: str) -> List[str]:
    with open(file, "r") as f:
        return f.read().split("\n\n")


def value_checker(dct: Dict[str, str]) -> Union[bool, Match[str], None]:
    return (
        1920 <= int(dct["byr"]) <= 2002
        and 2010 <= int(dct["iyr"]) <= 2020
        and 2020 <= int(dct["eyr"]) <= 2030
        and (m1 := re.match(r"^(\d+)(cm|in)$", dct["hgt"]))
        and (
            (m1[2] == "cm" and 150 <= int(m1[1]) <= 193)
            or (m1[2] == "in" and 59 <= int(m1[1]) <= 76)
        )
        and re.match("^#[a-f0-9]{6}$", dct["hcl"])
        and dct["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        and re.match("^[0-9]{9}$", dct["pid"])
    )


def solver(s: List[str]) -> int:
    total = 0
    for p in s:
        p = p.replace("\n", " ").strip()
        check = [a.split(":") for a in p.split(" ")]
        passw_dict = {k: v for k, v in check}
        if passw_dict.keys() >= REQUIRED and value_checker(passw_dict):
            total += 1
    return total


if __name__ == "__main__":
    print(solver(file_reader(file)))
