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
    current = list(seats)
    final = list(seats)
    while current != final:
        for _, row in enumerate(seats):
            for _, seat in enumerate(row):
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
                    # if (
                    #     sum(
                    #         1
                    #         if occupied in (seats[x - 1][y - 1] or ["0"])
                    #         else 0 or 1
                    #         if occupied in (seats[x - 1] or ["0"])
                    #         else 0 or 1
                    #         if occupied in (seats[y - 1] or ["0"])
                    #         else 0 or 1
                    #         if occupied in (seats[x + 1][y + 1] or ["0"])
                    #         else 0 or 1
                    #         if occupied in (seats[x + 1][y - 1] or ["0"])
                    #         else 0 or 1
                    #         if occupied in (seats[x - 1][y + 1] or ["0"])
                    #         else 0 or 1
                    #         if occupied in (seats[x + 1] or ["0"])
                    #         else 0 or 1
                    #         if occupied in (seats[y + 1] or ["0"])
                    #         else 0,
                    #     )
                    #     >= 4
                    # ):
                    seat = empty
                elif seat == floor:
                    seat = floor

    return count


if __name__ == "__main__":
    print(solver(file_reader(file)))
