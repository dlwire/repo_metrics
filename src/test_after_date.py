import unittest
from datetime import datetime
from test_support import Changeset
from filters import after_date


class TestAfterDate(unittest.TestCase): 
    def setUp(self):
        self.OCT_2_1980_EPOCH = 339292800
        self.OCT_3_1980_EPOCH = 339379200
        self.OCT_2_1980_DATE = datetime(1980, 10, 2)
        self.OCT_3_1980_DATE = datetime(1980, 10, 3)

    def test_changeset_before_date_false(self):
        after_date_filter = after_date(self.OCT_3_1980_DATE)

        self.assertFalse(after_date_filter(Changeset(epochTime=self.OCT_2_1980_EPOCH)))

    def test_changeset_after_date_true(self):
        after_date_filter = after_date(self.OCT_2_1980_DATE)

        self.assertTrue(after_date_filter(Changeset(epochTime=self.OCT_3_1980_EPOCH)))

    def test_changeset_exactly_on_date_false(self):
        after_date_filter = after_date(self.OCT_3_1980_DATE) 
        
        self.assertFalse(after_date_filter(Changeset(epochTime=self.OCT_3_1980_EPOCH)))
