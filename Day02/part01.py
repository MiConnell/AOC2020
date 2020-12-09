import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    total = 0
    for line in s.splitlines():
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
    print(solver(file_reader(file)))
