import unittest
import calc_age
from datetime import datetime

class TestCalcAge(unittest.TestCase):
    
    def setUp(self):

        cur_year = datetime.now().year

        self.ages = [year for year in range(cur_year - 150, cur_year + 1)]
    def test_calculate_age_valid(self):

        for age in self.ages:
            self.assertEqual(calc_age.calculate_age(age), datetime.now().year - age)
        
if __name__ == "__main__":
    unittest.main()
