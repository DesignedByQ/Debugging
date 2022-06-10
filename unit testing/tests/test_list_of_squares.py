from program import list_of_squares

def test_nums():
    assert list_of_squares.list_of_squares(3) == {1: 1, 2: 4, 3: 9}