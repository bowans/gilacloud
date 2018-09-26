import unittest
from .solver import sum_of_multiples_3_5

class TestSum(unittest.TestCase):
    def test_10(self):
        ret = sum_of_multiples_3_5(10)
        self.assertEqual(23, ret)

    def test_1000(self):
        ret = sum_of_multiples_3_5(1000)
        self.assertEqual(233168, ret)
