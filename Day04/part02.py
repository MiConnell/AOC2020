import re
from typing import Dict

REQUIRED = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}

allowed_chars = {"0123456789abcdef"}


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


def value_checker(dct: Dict[str, str]) -> bool:
    if (
        dct.keys() >= REQUIRED
        and 1920 <= int(dct["byr"]) <= 2002
        and 2010 <= int(dct["iyr"]) <= 2020
        and 2020 <= int(dct["eyr"]) <= 2030
        and (m1 := re.match(r"^(\d+)(cm|in)$", dct["hgt"]))
        and (
            m1[2] == "cm"
            and 150 <= int(m1[1]) <= 193
            or m1[2] == "in"
            and 59 <= int(m1[1]) <= 76
        )
        and re.match("^#[a-f0-9]{6}$", dct["hcl"])
        and dct["ecl"] in set("amb blu brn gry grn hzl oth".split())
        and re.match("^[0-9]{9}$", dct["pid"])
    ):
        return True
    return False


def passport_validator(file: str) -> int:
    total = 0
    with open(file, "r") as f:
        passports = f.read().split("\n\n")
        for p in passports:
            p = p.replace("\n", " ").strip()
            check = [a.split(":") for a in p.split(" ")]
            passw_dict = {k: v for k, v in check}
            if passw_dict.keys() >= REQUIRED and value_checker(passw_dict):
                total += 1
    return total


if __name__ == "__main__":
    print(passport_validator("./blob.txt"))
