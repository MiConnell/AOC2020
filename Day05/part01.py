from typing import List


def bin_search(lst: List[int]) -> int:
    left: int = 0
    right = lst.index(lst[-1])
    return left + (right - left) // 2


def row_finder(row_string: str) -> int:
    row_range = list(range(128))
    rows = []
    for s in row_string:
        if s == "B":
            row_range = row_range[bin_search(row_range) + 1 :]
        elif s == "F":
            row_range = row_range[: bin_search(row_range)]
        rows.append(row_range)
    return [r for r in rows if len(r) == 1][0][0]


def column_finder(column_string: str) -> int:
    column_range = list(range(8))
    columns = []
    for s in column_string:
        if s == "R":
            column_range = column_range[bin_search(column_range) + 1 :]
        elif s == "L":
            column_range = column_range[: bin_search(column_range)]
        columns.append(column_range)
    return [c for c in columns if len(c) == 1][0][0]


def seat_checker(file: str) -> int:
    with open(file, "r") as f:
        total = [
            (row_finder(options[:7]) * 8) + column_finder(options[-3:])
            for options in f.readlines()
        ]

    return max(total)


if __name__ == "__main__":
    print(seat_checker("./blob.txt"))
