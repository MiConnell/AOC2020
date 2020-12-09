import os

file = os.path.join(os.path.dirname(__file__), "blob.txt")


def file_reader(file: str) -> str:
    with open(file, "r") as f:
        return f.read()


def solver(s: str) -> int:
    return sum(
        len(
            {
                (let, letter.count(let))  # type: ignore
                for let in letter  # type: ignore
                if letter.count(let) == value  # type: ignore
            },
        )
        for (letter, value) in [
            (a.replace("\n", ""), len(a.split("\n"))) for a in s.strip().split("\n\n")
        ]
    )


if __name__ == "__main__":
    print(solver(file_reader(file)))
