from cord1 import Coord, line_length

def test_a1():
    a1 = Coord(1,2)
    a2 = Coord(2,2)
    assert line_length(a1, a2) == 5

def test_a2():
    a1 = Coord(1,2)
    a2 = Coord(2,2)
    assert line_length(a1, a2) == 6


if __name__ == '__main__':
    test_a1()