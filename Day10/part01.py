import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    adapters = sorted([int(n) for n in s.splitlines()])
    current_heh = 0
    total = {1: 0, 2: 0, 3: 1}
    for jolty in adapters:
        total[jolty - current_heh] += 1
        current_heh = jolty
    if total[1] != 0 and total[2] != 0 and total[3] != 0:
        return total[1] * total[2] * total[3]
    elif total[1] == 0:
        return total[2] * total[3]
    elif total[2] == 0:
        return total[1] * total[3]
    return 0


if __name__ == "__main__":
    print(solver(file_reader(file)))
