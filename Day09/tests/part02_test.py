import os

import part02

test_file = os.path.join(os.path.dirname(__file__), "test_blob.txt")


def test_part01():
    assert part02.solver(test_file) == 8
