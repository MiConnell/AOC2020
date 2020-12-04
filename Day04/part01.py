def passport_validator(file: str) -> int:
    total = 0
    with open(file, "r") as f:
        passports = [p.split("\n \n") for p in f.readlines()]
        print(passports)
    return total


if __name__ == "__main__":
    print(passport_validator("./blob.txt"))
