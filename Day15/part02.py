import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    seen = [(int(n), i) for i, n in enumerate(s.strip().split(","), 1)]
    last_idx = seen[-1][1]
    while len(seen) < 30_000_000:
        last_num = seen[-1][0]
        if last_num in [se[0] for se in seen[: last_idx - 1]]:
            contenders = [c for c in seen[: last_idx - 1] if c[0] == last_num]
            seen.append((last_idx - contenders[-1][1], last_idx + 1))
        else:
            seen.append((0, last_idx + 1))
        last_idx += 1
    return seen[-1][0]


if __name__ == "__main__":
    print(solver(file_reader(file)))
