import part02

test_file = os.path.join(os.path.dirname(__file__), "blob.txt")


def test_part02():
    assert part02.password_validator(test_file) == 1
