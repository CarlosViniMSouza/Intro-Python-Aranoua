# code of unittest docs

import unittest
from atv01test import sumNums, divIntNums

class TestStringMethods(unittest.TestCase):

    def testUpper(self):
        self.assertEqual('testing'.upper(), 'TESTING')

    def testIsupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


class TestResultOperations(unittest.TestCase):
    def testSum(self):
        self.assertEqual(sumNums(4, 6), 10)

    def testDivInt(self):
        self.assertFalse(divIntNums(4, 6), 2)


if __name__ == '__main__':
    unittest.main()
