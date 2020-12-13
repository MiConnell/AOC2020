import os

from sympy.ntheory.modular import crt

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    bus_ids = [
        (int(bus), i)
        for i, bus in enumerate(s.splitlines()[1].split(","))
        if bus != "x"
    ]
    busses = [b[0] for b in bus_ids]
    final = [-1 * b[1] for b in bus_ids]
    return crt(busses, final)[0]


if __name__ == "__main__":
    print(solver(file_reader(file)))
