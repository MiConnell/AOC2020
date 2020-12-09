import os

from part01 import bag_check
from part01 import file_reader

test_file = os.path.join(os.path.dirname(__file__), "test_blob.txt")


def test_part01():
    assert bag_check(file_reader(test_file)) == 4
