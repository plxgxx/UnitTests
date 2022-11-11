import unittest
from cord1 import Coord, line_length

class TestLineLength(unittest.TestCase):
    #Цифра в кінці тесту означає точку що тестимо
    def test_equalydiffx1(self): # від зміни х результат тесту незмінний
        a1 = Coord(1, 2)
        a2 = Coord(2, 2)
        self.assertEqual(5, line_length(a1, a2))

    def test_equalxdiffy1(self): # від зміни у результат тесту незмінний
        a1 = Coord(3, 0)
        a2 = Coord(3, 2)
        self.assertAlmostEquals(6.324555320, line_length(a1, a2))

    def test_diagonal1(self): # На діагоналях
        # незмінним залишається результат у протилежній
        # точці діагоналі,
        # тому треба перевірити 2 випадки
        a1 = Coord(1, 3)
        a2 = Coord(2, 2)
        self.assertAlmostEqual(5.83095189, line_length(a1, a2))

    def test_diagonal1opposite(self):
        a1 = Coord(3, 3)
        a2 = Coord(2, 2)
        self.assertAlmostEqual(7.071067811, line_length(a1, a2))

    def test_equalCoords(self):
        a1 = Coord(2, 2)
        a2 = Coord(2, 2)
        self.assertAlmostEqual(5.6568542, line_length(a1, a2))

    # З другою точкою перевіряю від'ємні значення
    def test_equalydiffx2(self):
        a1 = Coord(2, 2)
        a2 = Coord(-3, 2)
        self.assertAlmostEqual(4.123105625, line_length(a1, a2))

    def test_equalxdiffy2(self):
        a1 = Coord(2, -2)
        a2 = Coord(2, 2)
        self.assertEquals(4, line_length(a1, a2))

    def test_oppositeCoords(self):
        a1 = Coord(2, 2)
        a2 = Coord(-2, -2)
        self.assertEquals(0, line_length(a1, a2))#Гіпотенуза неможлива там де точки лежать на 1 прямій
