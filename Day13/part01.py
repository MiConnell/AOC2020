import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    timestamp = int(s.splitlines()[0])
    final_timestamp = timestamp
    bus_ids = [int(bus) for bus in s.splitlines()[1].split(",") if bus != "x"]
    max_mod = 0
    curr_bus = 0
    for bus in bus_ids:
        if (mod := timestamp % bus) > max_mod:
            max_mod = mod
            curr_bus = bus
    while final_timestamp % curr_bus != 0:
        final_timestamp += 1
    return (final_timestamp - timestamp) * curr_bus


if __name__ == "__main__":
    print(solver(file_reader(file)))
