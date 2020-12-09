import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    maximum = 0
    for options in s.splitlines():
        options = (
            options.strip()
            .replace("F", "0")
            .replace("B", "1")
            .replace("L", "0")
            .replace("R", "1")
        )
        maximum = max(maximum, int(options, 2))

    return maximum


if __name__ == "__main__":
    print(solver(file_reader(file)))


"""
FFBBFFFRRL
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
"""
