import part02

test_file = "tests/test_blob.txt"


def test_part02():
    assert part02.answer_checker(test_file) == 6
