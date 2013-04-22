import unittest
from test_support import Changeset
from filters import *
from fickle import Fickle

OCT_2_1980_EPOCH = 339292800
OCT_3_1980_DATE = datetime(1980, 10, 3)

class TestFilterChangesets(unittest.TestCase):
    def setUp(self):
        self.changesets = [Changeset(filepaths=['test']),
                           Changeset(filepaths=['test'], epochTime=OCT_2_1980_EPOCH),
                           Changeset(filepaths=['test'], branch='another branch'),
                           Changeset(filepaths=['code'])]

        self.fickle = Fickle('.')
        self.fickle.changesets = lambda: self.changesets

    def test_no_filters_returns_all_changesets(self):
        self.assertEquals(self.changesets, self.fickle.filter_changesets([]))

    def test_one_filter_returns_changsets_passing_that_filter(self):
        changesetsOnDefault = self.changesets[0:2] + self.changesets[3:4]
        self.assertEquals(changesetsOnDefault, self.fickle.filter_changesets([on_default]))

    def test_two_filters_returns_changesets_passing_both(self):
        changesetsOnDefaultAndTDDed = self.changesets[:2]
        self.assertEquals(changesetsOnDefaultAndTDDed, self.fickle.filter_changesets([is_tdded, on_default]))

    def test_three_filters_returns_changets_passing_all(self):
        changesetsOnDefaultAndTDDedSinceOct31980 = self.changesets[:1]

        filters = [is_tdded, on_default, after_date(OCT_3_1980_DATE)]
        self.assertEquals(changesetsOnDefaultAndTDDedSinceOct31980, self.fickle.filter_changesets(filters))

if __name__ == '__main__':
    unittest.main()
