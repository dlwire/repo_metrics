import unittest
from test_support import Changeset
from datetime import datetime
from run_metrics import parse_arguments

class TestParseArguments(unittest.TestCase):
    def setUp(self):
        self.OCT_2_1980_EPOCH = 339292800
        self.OCT_3_1980_EPOCH = 339379200

    def test_no_arguments_returns_default_filters(self):
        filters = parse_arguments(['script_name.py'])
        
        self.assertEquals(1, len(filters))
        self.assertEquals('On Branch: default', filters[0].__str__())

    def test_date_argument_returns_a_filter(self):
        filters = parse_arguments(['script_name.py', '--afterDate', '1980-10-2'])
        
        self.assertEquals(2, len(filters))
        self.assertEquals('After Date: 1980-10-02', filters[0].__str__())
        self.assertEquals('On Branch: default', filters[1].__str__())

    def test_user_argument_returns_a_filter(self):
        filters = parse_arguments(['script_name.py', '--users', 'A User'])

        self.assertEquals(2, len(filters))
        self.assertEquals('Users: A User', filters[0].__str__())
        self.assertEquals('On Branch: default', filters[1].__str__())

    def test_user_argument_passes_multiple_users(self):
        filters = parse_arguments(['script_name.py', '--users', 'A User', 'B User'])

        self.assertEquals(2, len(filters))
        self.assertEquals('Users: A User, B User', filters[0].__str__())
        self.assertEquals('On Branch: default', filters[1].__str__())

    def test_handles_multiple_arguments(self):
        filters = parse_arguments(['script_name.py', '--users', 'A User', '--afterDate', '1980-10-2'])

        self.assertEquals(3, len(filters))
        self.assertEquals('After Date: 1980-10-02', filters[0].__str__())
        self.assertEquals('Users: A User', filters[1].__str__())
        self.assertEquals('On Branch: default', filters[2].__str__())

    def test_file_extension_argument_returns_a_filter(self):
        filters = parse_arguments(['script_name.py', '--extensions', 'cpp'])

        self.assertEquals(2, len(filters))
        self.assertEquals('Extensions: cpp', filters[0].__str__())
        self.assertEquals('On Branch: default', filters[1].__str__())
