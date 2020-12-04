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
