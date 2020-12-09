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
        first_index = int(params.split("-")[0]) - 1
        second_index = int(params.split("-")[-1]) - 1
        char = ln[1].replace(":", "")
        password = ln[-1]
        if (char == password[first_index]) ^ (char == password[second_index]):
            total += 1
    return total


if __name__ == "__main__":
    print(solver(file_reader(file)))
