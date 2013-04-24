import unittest
from datetime import datetime
from filters import after_date
from parse_arguments import parse_arguments

class TestParseArguments(unittest.TestCase):
    def test_no_arguments_returns_no_filters(self):
        self.assertEquals([], parse_arguments(['script_name.py']))

    def test_date_argument_returns_a_filter(self):
        self.assertEquals(1, len(parse_arguments(['script_name.py', "-afterDate'1980-10-2'"])))

    def test_user_argument_returns_a_filter(self):
        self.assertEquals(1, len(parse_arguments(['script_name.py', "-user'A User'"])))
