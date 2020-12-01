import itertools

def calculate(s: str, goal: int) -> int:
    nums = sorted([int(line) for line in open(s).readlines()], reverse=True)
    for a, b, c in itertools.combinations(nums, 3):
        if a + b + c == goal:
            return a * b * c
    return 0

if __name__ == "__main__":
    print(calculate('./blob.txt', 2020))
