# code of unittest docs

import unittest


class TestStringMethods(unittest.TestCase):

    def testUpper(self):
        self.assertEqual('testing'.upper(), 'TESTING')

    def testIsupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def testSplit(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
