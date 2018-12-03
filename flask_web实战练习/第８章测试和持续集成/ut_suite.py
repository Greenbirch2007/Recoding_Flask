

import unittest

from collections import Counter



class TestCounter(unittest.TestCase):
    def setUp(self):
        self.c = Counter('abcdaba')
        print('SetUp starting~~~~')

    def runTest(self):
        c = self.c
        self.assertEqual(c,Counter(a=3,b=2,c=1,d=1))

    def tearDown(self):
        print('tearDown starting~~~~')


if __name__ =='__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCounter()) # 可以用addTest添加更多的TestCase实例
    runner = unittest.TextTestRunner()
    runner.run(suite)
