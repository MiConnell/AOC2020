import part02

test_file = "tests/test_blob.txt"


def test_part02():
    assert part02.calculate(test_file, 2020) == 241861950
