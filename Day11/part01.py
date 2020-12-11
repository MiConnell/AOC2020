import os
from typing import List

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    seats = s.splitlines()
    x = 0
    y = 0
    count = 0
    empty = "L"
    occupied = "#"
    floor = "."
    for row in seats:
        for seat in row:
            if seat == empty:
                if occupied not in [
                    (seats[x - 1][y - 1] or seat),
                    (seats[x - 1] or seat),
                    (seats[y - 1] or seat),
                    (seats[x + 1][y + 1] or seat),
                    (seats[x + 1][y - 1] or seat),
                    (seats[x - 1][y + 1] or seat),
                    (seats[x + 1] or seat),
                    (seats[y + 1] or seat),
                ]:
                    seat = occupied
                    count += 1
            elif seat == occupied:
                if occupied in [
                    (seats[x - 1][y - 1] or seat),
                    (seats[x - 1] or seat),
                    (seats[y - 1] or seat),
                    (seats[x + 1][y + 1] or seat),
                    (seats[x + 1][y - 1] or seat),
                    (seats[x - 1][y + 1] or seat),
                    (seats[x + 1] or seat),
                    (seats[y + 1] or seat),
                ]:
                    seat = empty
                    count += 1
            elif seat == floor:
                seat = floor

    return count


if __name__ == "__main__":
    print(solver(file_reader(file)))
