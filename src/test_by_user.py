import unittest
from test_support import Changeset
from filters import by_user

class TestByUser(unittest.TestCase):
    def test_not_matching_user_returns_false(self):
        self.assertFalse(by_user(['A User'])(Changeset(user='Another User')))

    def test_matching_user_returns_true(self):
        self.assertTrue(by_user(['A User'])(Changeset(user='A User')))

    def test_case_insensitive(self):
        self.assertTrue(by_user(['A USER'])(Changeset(user='A User')))

    def test_partial_matches(self):
        self.assertTrue(by_user(['user'])(Changeset(user='A User')))
