import unittest
from test_support import Changeset
from datetime import datetime
from filters import after_date
from parse_arguments import parse_arguments

class TestParseArguments(unittest.TestCase):
    def setUp(self):
        self.OCT_2_1980_EPOCH = 339292800
        self.OCT_3_1980_EPOCH = 339379200

    def test_no_arguments_returns_no_filters(self):
        filters = parse_arguments(['script_name.py'])
        self.assertEquals([], filters)

    def test_date_argument_returns_a_filter(self):
        filters = parse_arguments(['script_name.py', '--afterDate', '1980-10-2'])
        
        self.assertEquals(1, len(filters))
        self.assertFalse(filters[0](Changeset(epochTime=self.OCT_2_1980_EPOCH)))
        self.assertTrue(filters[0](Changeset(epochTime=self.OCT_3_1980_EPOCH)))

    def test_user_argument_returns_a_filter(self):
        filters = parse_arguments(['script_name.py', '--users', 'A User'])

        self.assertEquals(1, len(filters))
        self.assertFalse(filters[0](Changeset(user='Another User')))
        self.assertTrue(filters[0](Changeset(user='A User')))

    def test_user_argument_passes_multiple_users(self):
        filters = parse_arguments(['script_name.py', '--users', 'A User', 'B User'])

        self.assertEquals(1, len(filters))
        self.assertFalse(filters[0](Changeset(user='Another User')))
        self.assertTrue(filters[0](Changeset(user='A User')))
        self.assertTrue(filters[0](Changeset(user='B User')))

    def test_handles_multiple_arguments(self):
        filters = parse_arguments(['script_name.py', '--users', 'A User', '--afterDate', '1980-10-2'])

        self.assertEquals(2, len(filters))
        self.assertFalse(filters[0](Changeset(epochTime=self.OCT_2_1980_EPOCH)))
        self.assertTrue(filters[0](Changeset(epochTime=self.OCT_3_1980_EPOCH)))
        self.assertFalse(filters[1](Changeset(user='Another User')))
        self.assertTrue(filters[1](Changeset(user='A User')))

