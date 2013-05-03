import unittest
from test_support import Changeset
from filters import ByUsers

class TestByUsers(unittest.TestCase):
    def test_not_matching_user_returns_false(self):
        self.assertFalse(ByUsers(['A User'])(Changeset(user='Another User')))

    def test_matching_user_returns_true(self):
        self.assertTrue(ByUsers(['A User'])(Changeset(user='A User')))

    def test_case_insensitive(self):
        self.assertTrue(ByUsers(['A USER'])(Changeset(user='A User')))

    def test_partial_matches(self):
        self.assertTrue(ByUsers(['user'])(Changeset(user='A User')))

    def test_any_matching_user_passes(self):
        self.assertTrue(ByUsers(['A User', 'B User'])(Changeset(user='B User')))
