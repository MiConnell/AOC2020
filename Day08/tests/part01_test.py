import os

import part01

test_file = os.path.join(os.path.dirname(__file__), "test_blob.txt")


def test_part01():
    assert part01.solver(test_file) == 5