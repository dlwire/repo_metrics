import unittest
from repo_metrics import convert_to_percent

class TestConvertToPercent(unittest.TestCase):
    def test_0_0_throws_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: convert_to_percent(0, 0))

    def test_0_1_returns_0_percent(self):
        self.assertEquals(0, convert_to_percent(0, 1))

    def test_1_1_returns_100_percent(self):
        self.assertEquals(100, convert_to_percent(1, 1))

    def test_1_2_returns_50_percent(self):
        self.assertEquals(50, convert_to_percent(1, 2))

    def test_1_3_returns_33_percent(self):
        self.assertEquals(33, convert_to_percent(1, 3))

    def test_2_3_returns_66_percent(self):
        self.assertEquals(66, convert_to_percent(2, 3))

    def test_2_1_returns_200_percent(self):
        self.assertEquals(200, convert_to_percent(2, 1))
