def seat_checker(file: str) -> int:
    with open(file, "r") as f:
        maximum = 0
        seats = []
        for options in f.readlines():
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
    print(seat_checker("./blob.txt"))
