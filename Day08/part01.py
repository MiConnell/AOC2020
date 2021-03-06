import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    acc = 0
    seen_indexes = set()
    lines = [line for line in s.splitlines()]
    ind = 0
    while ind not in seen_indexes:
        op, val = lines[ind].split(" ")
        if op == "acc":
            acc += eval(val)
            seen_indexes.add(ind)
            ind += 1
        elif op == "jmp":
            seen_indexes.add(ind)
            ind += eval(val)
        elif op == "nop":
            seen_indexes.add(ind)
            ind += 1
    return acc


if __name__ == "__main__":
    print(solver(file_reader(file)))
