import re

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


def value_checker(key: str, val: str) -> bool:
    if key == "byr":
        return 1920 <= int(val) <= 2002
    if key == "iyr":
        return 2010 <= int(val) <= 2020
    if key == "eyr":
        return 2020 <= int(val) <= 2030
    if key == "hgt":
        if val[-2:] == "cm":
            return 150 <= int(val) <= 193
        elif val[-2:] == "in":
            return 59 <= int(val) <= 76
    if key == "hcl":
        return 150 <= int(val) <= 193
    if key == "ecl":
        return val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if key == "pid":
        if int(val[0]) == 0:
            return int(val[0:]) <= 99999999
        return 150 <= int(val) <= 193
    if key == "cid":
        print("uwu")
    return False


def passport_validator(file: str) -> int:
    total = 0
    with open(file, "r") as f:
        passports = f.read().split("\n\n")
        for p in passports:
            p = p.replace("\n", " ").strip()
            check = [a.split(":") for a in p.split(" ")]
            keys = []
            values = []
            passw_dict = {}
            for c in check:
                keys.append(c[0])
                values.append(c[1])
            for k, v in zip(keys, values):
                passw_dict[k] = v
    return total


if __name__ == "__main__":
    print(passport_validator("./blob.txt"))
