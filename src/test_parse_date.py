import unittest
from datetime import datetime
from run_metrics import parse_date

class TestParseDate(unittest.TestCase):
    def test_returns_datetime_matching_args(self):
        self.assertEquals(datetime(2012, 1, 1), parse_date('2012-01-01'))

    def test_returns_another_datetime(self):
        self.assertEquals(datetime(1980, 10, 2), parse_date('1980-10-02'))
