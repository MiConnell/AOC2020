import os
from typing import List
from typing import Tuple

file = os.path.join(os.path.dirname(__file__), "blob.txt")

swap = {"nop": "jmp", "jmp": "nop"}


def inf_index(file: List[Tuple[str, str]], f: int) -> int:
    acc = 0
    ind = 0
    seen_indexes = set()
    lines = [line for line in file]
    while ind not in seen_indexes and ind < len(lines):
        seen_indexes.add(ind)
        op, val = lines[ind][0], lines[ind][1]
        if ind == f:
            op = swap[op]
        if op == "acc":
            acc += eval(val)
            ind += 1
        elif op == "jmp":
            ind += eval(val)
        elif op == "nop":
            ind += 1
    if ind == len(lines):
        return acc
    else:
        raise RuntimeError(seen_indexes)


def solver(file: str) -> int:
    with open(file, "r") as f:
        lines = [line.strip().split(" ") for line in f.readlines()]
        options = [(__license__[0], __license__[1]) for __license__ in lines]
        try:
            inf_index(options, -1)
            seen_indexes = set()
        except Exception as e:
            (seen_indexes,) = e.args
    for i in seen_indexes:
        if options[i][0] in ["jmp", "noc"]:
            try:
                return inf_index(options, i)
            except Exception:
                pass
    return 0


if __name__ == "__main__":
    print(solver(file))
