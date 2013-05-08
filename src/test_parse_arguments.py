import unittest
from datetime import datetime
from test_support import Changeset
from run_metrics import parse_arguments

class TestParseArguments(unittest.TestCase):
    def setUp(self):
        self.OCT_2_1980_DATE = datetime(1980, 10, 2)

    def test_no_arguments_returns_default_branch(self):
        args = parse_arguments(['script_name.py'])
        
        self.assertEquals(None, args.afterDate)
        self.assertEquals(None, args.users)
        self.assertEquals(None, args.extensions)
        self.assertEquals('default', args.branch)
        self.assertEquals([], args.args)

    def test_date_arguments_populated_after_date_arg(self):
        args = parse_arguments(['script_name.py', '--afterDate', '1980-10-2'])
        
        self.assertEquals(self.OCT_2_1980_DATE, args.afterDate)
        self.assertEquals(None, args.users)
        self.assertEquals(None, args.extensions)
        self.assertEquals('default', args.branch)
        self.assertEquals([], args.args)

    def test_user_arguments_populated_users_arg(self):
        args = parse_arguments(['script_name.py', '--users', 'A User'])

        self.assertEquals(None, args.afterDate)
        self.assertEquals(['A User'], args.users)
        self.assertEquals(None, args.extensions)
        self.assertEquals('default', args.branch)
        self.assertEquals([], args.args)

    def test_user_argument_takes_multiple_users(self):
        args = parse_arguments(['script_name.py', '--users', 'A User', 'B User'])

        self.assertEquals(None, args.afterDate)
        self.assertEquals(['A User', 'B User'], args.users)
        self.assertEquals(None, args.extensions)
        self.assertEquals('default', args.branch)
        self.assertEquals([], args.args)

    def test_file_extension_populates_extensions_arg(self):
        args = parse_arguments(['script_name.py', '--extensions', 'cpp'])

        self.assertEquals(None, args.afterDate)
        self.assertEquals(None, args.users)
        self.assertEquals(['cpp'], args.extensions)
        self.assertEquals('default', args.branch)
        self.assertEquals([], args.args)

    def test_file_extension_handles_multiple_extensions(self):
        args = parse_arguments(['script_name.py', '--extensions', 'cpp', 'h'])

        self.assertEquals(None, args.afterDate)
        self.assertEquals(None, args.users)
        self.assertEquals(['cpp', 'h'], args.extensions)
        self.assertEquals('default', args.branch)
        self.assertEquals([], args.args)

    def test_handles_multiple_arguments(self):
        args = parse_arguments(['script_name.py', '--users', 'A User', '--afterDate', '1980-10-2'])

        self.assertEquals(self.OCT_2_1980_DATE, args.afterDate)
        self.assertEquals(['A User'], args.users)
        self.assertEquals(None, args.extensions)
        self.assertEquals('default', args.branch)
        self.assertEquals([], args.args)


