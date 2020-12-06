def answer_checker(file: str) -> int:
    with open(file, "r") as f:
        answers = [set(a.replace("\n", "")) for a in f.read().strip().split("\n\n")]
        return sum(len(ans) for ans in answers)


if __name__ == "__main__":
    print(answer_checker("./blob.txt"))
