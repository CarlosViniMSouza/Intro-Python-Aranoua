# code of unittest docs

import unittest
from atv01test import *

class TestStringMethods(unittest.TestCase):
    def testUpper(self):
        self.assertEqual('testing'.upper(), 'TESTING')

    def testIsupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


class TestResultOperations(unittest.TestCase):
    def testSum(self):
        self.assertEqual(sumNums(4, 6), 10)
        self.assertTrue(sumNums(7, 9) ==  16)
        self.assertFalse(sumNums(7, 9) > 16) 

    def testSub(self):
        self.assertEqual(subNums(4, 6), -2)

    def testMult(self):
        self.assertEqual(multNums(4, 6), 24)

    def testDivFrac(self):
        self.assertTrue(divFracNums(4, 6) >= 0)

    def testDivInt(self):
        self.assertTrue(divIntNums(4, 6) <= 2)

    def testMod(self):
        self.assertEqual(modNums(4, 8), 4)

    def testQuad(self):
        self.assertEqual(quadNum01(4), 16.0)


if __name__ == '__main__':
    unittest.main()
