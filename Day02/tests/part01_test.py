import part01

test_file = "tests/test_blob.txt"


def test_part01():
    assert part01.password_validator(test_file) == 2