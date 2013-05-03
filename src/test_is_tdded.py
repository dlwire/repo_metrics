import unittest
from test_support import Changeset
from filters import IsTdded
        
class TestIsTdded(unittest.TestCase):
    def setUp(self):
        self.testedFilter = IsTdded()

    def test_no_file_changes_is_not_tdd(self):
        self.assertFalse(self.testedFilter(Changeset(filepaths=[])))

    def test_only_test_file_is_considered_tdded(self):
        self.assertTrue(self.testedFilter(Changeset(filepaths=['filetest'])))

    def test_does_not_care_about_case(self):
        self.assertTrue(self.testedFilter(Changeset(filepaths=['FILETEST'])))

    def test_only_code_file_is_not_tdded(self):
        self.assertFalse(self.testedFilter(Changeset(filepaths=['filecode'])))

    def test_code_and_test_testedFilter(self):
        self.assertTrue(self.testedFilter(Changeset(filepaths=['filecode', 'testcode'])))
