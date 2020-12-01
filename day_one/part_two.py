def calculate(s: str, goal: int) -> int:
    nums = [int(line) for line in open(s).readlines()]
    for n in nums:
        if goal - n in nums:
            return (goal - n) * n
    return 0

if __name__ == "__main__":
    print(calculate('./blob.txt', 2020))
