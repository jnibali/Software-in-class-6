import unittest
import leap_year

class testCaseAdd(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(leap_year.leapyear(2004),"is a leap year")
        self.assertEqual(leap_year.leapyear(2012),"is a leap year")
        self.assertEqual(leap_year.leapyear(2007),"is not a leap year")
        self.assertEqual(leap_year.leapyear(2001),"is not a leap year")

#tests for additon, then subtraction, then multiply, and then division
#select right options in terminal when testing

if __name__ == '__main__':
    unittest.main()