import os

import part02

test_file = os.path.join(os.path.dirname(__file__), "blob.txt")


def test_part02():
    assert part02.calculate(test_file, 2020) == 241861950
