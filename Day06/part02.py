def counter(lst: list) -> int:
    total = [(let, lst[0].count(let)) for let in lst[0] if lst[0].count(let) == lst[1]]

    return len(set(total))


def answer_checker(file: str) -> int:
    with open(file, "r") as f:
        answers = []
        for a in f.read().strip().split("\n\n"):
            count = len(a.split("\n"))
            answers.append([a.replace("\n", ""), count])
        total = sum(counter(ans) for ans in answers)
    return total


if __name__ == "__main__":
    print(answer_checker("./blob.txt"))
