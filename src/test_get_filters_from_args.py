import unittest
from datetime import datetime
from test_support import ParsedArgumentsMock
from run_metrics import get_filters_from_args

class TestGetFiltersFromArgs(unittest.TestCase):
    def setUp(self):
        self.OCT_2_1980_DATE = datetime(1980, 10, 2)

    def test_default_mock_has_branch_set_to_default(self):
        filters = get_filters_from_args(ParsedArgumentsMock())

        self.assertEquals(1, len(filters))
        self.assertEquals('On Branch: default', filters[0].__str__())

    def test_after_date_argument_generates_date_issue(self):
        filters = get_filters_from_args(ParsedArgumentsMock(afterDate=self.OCT_2_1980_DATE))

        self.assertEquals(2, len(filters))
        self.assertEquals('After Date: 1980-10-02', filters[0].__str__())
        self.assertEquals('On Branch: default', filters[1].__str__())

    def test_user_argument_generates_single_user_filter(self):
        filters = get_filters_from_args(ParsedArgumentsMock(users=['A User']))

        self.assertEquals(2, len(filters))
        self.assertEquals('Users: A User', filters[0].__str__())
        self.assertEquals('On Branch: default', filters[1].__str__())

    def test_user_argument_handles_multiple_arguments(self):
        filters = get_filters_from_args(ParsedArgumentsMock(users=['A User', 'B User']))

        self.assertEquals(2, len(filters))
        self.assertEquals('Users: A User, B User', filters[0].__str__())
        self.assertEquals('On Branch: default', filters[1].__str__())

    def test_extensions_argument_generates_an_extension_filter(self):
        filters = get_filters_from_args(ParsedArgumentsMock(extensions = ['cpp']))

        self.assertEquals(2, len(filters))
        self.assertEquals('Extensions: cpp', filters[0].__str__())
        self.assertEquals('On Branch: default', filters[1].__str__())

    def test_handles_multiple_extensions(self):
        filters = get_filters_from_args(ParsedArgumentsMock(extensions = ['cpp', 'h']))

        self.assertEquals(2, len(filters))
        self.assertEquals('Extensions: cpp, h', filters[0].__str__())
        self.assertEquals('On Branch: default', filters[1].__str__())

    def test_generates_filters_for_multiple_arguments(self):
        filters = get_filters_from_args(ParsedArgumentsMock(users=['A User'], afterDate=self.OCT_2_1980_DATE))

        self.assertEquals(3, len(filters))
        self.assertEquals('After Date: 1980-10-02', filters[0].__str__())
        self.assertEquals('Users: A User', filters[1].__str__())
        self.assertEquals('On Branch: default', filters[2].__str__())


