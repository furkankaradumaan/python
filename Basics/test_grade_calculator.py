import unittest
from grade_calculator import *


class TestGradeCalculator(unittest.TestCase):

    def test_calculate_letter_grade(self):

        aa = [i for i in range(90, 101)]
        ba = [i for i in range(80, 90)]
        bb = [i for i in range(70, 80)]
        cb = [i for i in range(60 ,70)]
        cc = [i for i in range(50, 60)]
        dc = [i for i in range(40, 50)]
        ff = [i for i in range(0, 40)]

        for i in range(0, 101):
            equals = None
            if i in aa:
                equals = "AA"
            elif i in ba:
                equals = "BA"
            elif i in bb:
                equals = "BB"
            elif i in cb:
                equals = "CB"
            elif i in cc:
                equals = "CC"
            elif i in dc:
                equals = "DC"
            elif i in ff:
                equals = "FF"
            
            self.assertEqual(calculate_letter_grade(i), equals)


if __name__ == '__main__':
    unittest.main()


