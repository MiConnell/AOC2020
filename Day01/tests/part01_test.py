import part01

test_file = "tests/test_blob.txt"


def test_part01():
    assert part01.calculate(test_file, 2020) == 514579
