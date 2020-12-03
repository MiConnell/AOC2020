def password_validator(file: str) -> int:
    with open(file, "r") as f:
        total = 0
        for line in f.readlines():
            line = line.split()
            params = line[0]
            min_ = int(params.split("-")[0])
            max_ = int(params.split("-")[-1])
            char = line[1].replace(":", "")
            password = line[-1]
            if char in password and min_ <= password.count(char) <= max_:
                total += 1
    return total


if __name__ == "__main__":
    print(password_validator("./blob.txt"))
