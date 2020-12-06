def password_validator(file: str) -> int:
    with open(file, "r") as f:
        total = 0
        for line in f.readlines():
            ln = line.split()
            params = ln[0]
            min_ = int(params.split("-")[0])
            max_ = int(params.split("-")[-1])
            char = ln[1].replace(":", "")
            password = ln[-1]
            if char in password and min_ <= password.count(char) <= max_:
                total += 1
    return total


if __name__ == "__main__":
    print(password_validator("./blob.txt"))
