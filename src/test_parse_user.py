import unittest
from parse_arguments import parse_user

class TestParseUser(unittest.TestCase):
    def test_returns_string_of_username_part(self):
        self.assertEquals(['A. Username'], parse_user("-user'A. Username'"))

    def test_returns_multiple_username_parts(self):
        self.assertEquals(['A. Username', 'B. Username'], parse_user("-user-'A. Username, B. Username'"))
