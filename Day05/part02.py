import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    maximum = 0
    seats = []
    for options in s.splitlines():
        options = (
            options.strip()
            .replace("F", "0")
            .replace("B", "1")
            .replace("L", "0")
            .replace("R", "1")
        )
        seats.append(int(options, 2))
        maximum = max(maximum, int(options, 2))

    for i in range(min(seats), maximum):
        if i not in seats:
            return i
    return 0


if __name__ == "__main__":
    print(solver(file_reader(file)))
