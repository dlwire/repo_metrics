import unittest
from test_support import Changeset
from filters import is_tdded
        
class TestIsTdded(unittest.TestCase):
    def test_no_file_changes_is_not_tdd(self):
        self.assertFalse(is_tdded(Changeset(filepaths=[])))

    def test_only_test_file_is_considered_tdded(self):
        self.assertTrue(is_tdded(Changeset(filepaths=['filetest'])))

    def test_does_not_care_about_case(self):
        self.assertTrue(is_tdded(Changeset(filepaths=['FILETEST'])))

    def test_only_code_file_is_not_tdded(self):
        self.assertFalse(is_tdded(Changeset(filepaths=['filecode'])))

    def test_code_and_test_is_tdded(self):
        self.assertTrue(is_tdded(Changeset(filepaths=['filecode', 'testcode'])))
