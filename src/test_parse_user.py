import unittest
from parse_arguments import parse_user

class TestParseUser(unittest.TestCase):
    def test_returns_string_of_username_part(self):
        self.assertEquals('A. Username', parse_user("-user'A. Username'"))
