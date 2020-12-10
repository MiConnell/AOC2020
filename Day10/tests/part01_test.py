import os

from part01 import file_reader
from part01 import solver

test_file = os.path.join(os.path.dirname(__file__), "test_blob.txt")


def test_part01():
    assert solver(file_reader(test_file)) == 35
