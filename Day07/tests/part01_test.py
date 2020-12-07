import part01

test_file = "tests/test_blob.txt"


def test_part01():
    assert part01.answer_checker(test_file) == 11
