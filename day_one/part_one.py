def calculate(s: str, goal: int) -> int:
    nums = []
    with open(s, 'r') as f:
        for line in f.readlines():
            line = int(line)
            nums.append(line)
    for n in nums:
        if goal - n in nums:
            return (goal - n) * n
    return 0

if __name__ == "__main__":
    print(calculate('./blob.txt', 2020))
