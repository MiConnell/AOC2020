REQUIRED = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}


def passport_validator(file: str) -> int:
    total = 0
    with open(file, "r") as f:
        passports = f.read().split("\n\n")
        for p in passports:
            p = p.replace("\n", " ").strip()
            check = [a.split(":")[0] for a in p.split(" ")]
            if "cid" in check:
                check.remove("cid")
            if len(list(set(check))) > 6:
                total += 1
    return total


if __name__ == "__main__":
    print(passport_validator("./blob.txt"))
