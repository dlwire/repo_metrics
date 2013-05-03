import unittest
from test_support import Changeset
from filters import ByExtensions

class TestByExtensions(unittest.TestCase):
    def test_not_matching_extension_returns_false(self):
        self.assertFalse(ByExtensions(['cpp'])(Changeset(['script.py'])))

    def test_matching_extensions_returns_true(self):
        self.assertTrue(ByExtensions(['h'])(Changeset(['headerfile.h'])))

    def test_will_match_any_of_multiple_files(self):
        self.assertTrue(ByExtensions(['py'])(Changeset(['codefile.cpp', 'script.py'])))

    def test_matching_extension_must_be_at_end_preceeded_by_point(self):
        self.assertFalse(ByExtensions(['cpp'])(Changeset(['noextensioncpp'])))

    def test_matches_with_any_of_multiple_extensions(self):
        self.assertTrue(ByExtensions(['py', 'cpp'])(Changeset(['codefile.cpp'])))
