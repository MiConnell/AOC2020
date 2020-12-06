def answer_checker(file: str) -> int:
    with open(file, "r") as f:
        return sum(
            len(
                {
                    (let, letter.count(let))  # type: ignore
                    for let in letter  # type: ignore
                    if letter.count(let) == value  # type: ignore
                },
            )
            for (letter, value) in [
                (a.replace("\n", ""), len(a.split("\n")))
                for a in f.read().strip().split("\n\n")
            ]
        )


if __name__ == "__main__":
    print(answer_checker("./blob.txt"))
