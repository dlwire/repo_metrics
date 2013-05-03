import unittest
from repo_metrics import get_count_and_percentage

class TestGetCountAndPercentage(unittest.TestCase):
    def test_handles_no_incoming_changesets(self):
        self.assertEquals((0,0), get_count_and_percentage([], lambda x: True))

    def test_for_full_pass_filter_returns_all_changesets_and_100(self):
        self.assertEquals((2, 100), get_count_and_percentage(['dont', 'care'], lambda x: True))

    def test_for_no_pass_filter_returns_0_and_0(self):
        self.assertEquals((0, 0), get_count_and_percentage(['dont', 'care'], lambda x: False))

    def test_for_half_pass_filter_returns_1_and_50(self):
        self.assertEquals((1, 50), get_count_and_percentage(['pass', 'no'], lambda x: x == 'pass'))

if __name__ == '__main__':
    unittest.main()
