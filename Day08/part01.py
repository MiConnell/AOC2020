import os
import re

file = os.path.join(os.path.dirname(__file__), "blob.txt")
# file = "./tests/test_blob.txt"


def bag_check(file: str) -> int:
    with open(file, "r") as f:
        bag_list = set()
        for line in f.readlines():
            main_bag, inner = (
                re.sub(r"[0-9]+", "", line)
                .strip()
                .replace("bags", "bag")
                .strip()
                .split("contain")
            )
            inner_fmt = (
                inner.strip().replace("bags", "bag").replace(".", "").split(", ")
            )
            if "shiny gold bag" in inner_fmt:
                bag_list.add(main_bag)
            for i in inner_fmt:
                if i in bag_list:
                    bag_list.add(main_bag)
        return len(bag_list)


if __name__ == "__main__":
    print(bag_check(file))


"""
light red bag    | [bright white bag, muted yellow bag]  x
dark orange bag  | [bright white bag, muted yellow bag]  x
bright white bag | [shiny gold bag]                      x
muted yellow bag | [shiny gold bag, faded blue bag]      x
shiny gold bag   | [dark olive bag, vibrant plum bag]
dark olive bag   | [faded blue bag, dotted black bag]
vibrant plum bag | [faded blue bag, dotted black bag]
faded blue bag   | [no other bag]
dotted black bag | [no other bag]
"""
# loop through main first, then inner?
