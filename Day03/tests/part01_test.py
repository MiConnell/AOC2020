import part01

test_file = os.path.join(os.path.dirname(__file__), "blob.txt")


def test_part01():
    assert part01.tree_counter(test_file) == 7
