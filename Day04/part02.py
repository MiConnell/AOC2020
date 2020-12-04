from typing import Dict

from future.types import issubset

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


def value_checker(d: Dict[str, str]) -> bool:
    result = False
    for key, val in d.items():
        try:
            if key == "byr" and 1920 <= int(val) <= 2002:
                result = True
            if key == "iyr" and 2010 <= int(val) <= 2020:
                result = True
            if key == "eyr" and 2020 <= int(val) <= 2030:
                result = True
            if key == "hgt":
                if val[-2:] == "cm" and 150 <= int(val) <= 193:
                    result = True
                elif val[-2:] == "in" and 59 <= int(val) <= 76:
                    result = True
            if key == "hcl" and val[0] == "#" and set(val[0:]).issubset(allowed_chars):
                result = True
            if key == "ecl" and val in [
                "amb",
                "blu",
                "brn",
                "gry",
                "grn",
                "hzl",
                "oth",
            ]:
                result = True
            if key == "pid":
                if int(val[0]) == 0:
                    return int(val[0:]) <= 99999999
                else:
                    return int(val) <= 99999999
        except ValueError:
            result = False
    return result


def passport_validator(file: str) -> int:
    total = 0
    with open(file, "r") as f:
        passports = f.read().split("\n\n")
        for p in passports:
            p = p.replace("\n", " ").strip()
            check = [a.split(":") for a in p.split(" ")]
            if len(check) > 6:
                keys = []
                values = []
                for c in check:
                    keys.append(c[0])
                    values.append(c[1])
                passw_dict = {k: v for k, v in zip(keys, values)}
                if value_checker(passw_dict):
                    total += 1
    return total


if __name__ == "__main__":
    print(passport_validator("./blob.txt"))
