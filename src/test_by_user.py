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

    def test_str_returns_description_of_filter_for_one_user(self):
        users_filter = ByUsers(['A User'])

        self.assertEquals('Users: A User', users_filter.__str__())

    def test_str_returns_description_of_filter_for_multiple_users(self):
        users_filter = ByUsers(['A User', 'B User'])

        self.assertEquals('Users: A User, B User', users_filter.__str__())
