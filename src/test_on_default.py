import unittest
from test_support import Changeset
from filters import OnBranch

class TestOnDefault(unittest.TestCase):
    def setUp(self):
        self.default_filter = OnBranch('default')
        self.other_filter = OnBranch('other')

    def test_default_branch_returns_true(self):
        self.assertTrue(self.default_filter(Changeset(branch='default')))

    def test_other_branch_returns_false(self):
        self.assertFalse(self.default_filter(Changeset(branch='other')))

    def test_filter_branch_other_than_default(self):
        self.assertTrue(self.other_filter(Changeset(branch='other')))

if __name__ == '__main__':
    unittest.main()
