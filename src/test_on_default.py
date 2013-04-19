import unittest
from test_support import Changeset
from filters import on_default

class TestOnDefault(unittest.TestCase):
    def test_default_branch_returns_true(self):
        self.assertTrue(on_default(Changeset(branch='default')))

    def test_other_branch_returns_false(self):
        self.assertFalse(on_default(Changeset(branch='other branch')))

if __name__ == '__main__':
    unittest.main()
