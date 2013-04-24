import unittest
from test_support import Changeset
from filters import by_user

class TestByUser(unittest.TestCase):
    def test_not_matching_user_returns_false(self):
        self.assertFalse(by_user('A User')(Changeset(user='Another User')))

    def test_matching_user_returns_true(self):
        self.assertTrue(by_user('A User')(Changeset(user='A User')))
