import os

from part02 import file_reader
from part02 import solver

test_file = os.path.join(os.path.dirname(__file__), "test_blob.txt")


def test_part02():
    assert solver(file_reader(test_file)) == 336
