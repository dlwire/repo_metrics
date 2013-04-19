import unittest
from test_support import Changeset
from filters import *
from repo_metrics import filter_changesets

OCT_2_1980_EPOCH = 339292800
OCT_3_1980_DATE = datetime(1980, 10, 3)

class TestFilterChangesets(unittest.TestCase):
    def setUp(self):
        self.changesets = [Changeset(filepaths=['test']),
                           Changeset(filepaths=['test'], epochTime=OCT_2_1980_EPOCH),
                           Changeset(filepaths=['test'], branch='another branch'),
                           Changeset(filepaths=['code'])]

    def test_no_filters_returns_all_changesets(self):
        self.assertEquals(self.changesets, filter_changesets(self.changesets, []))

    def test_one_filter_returns_changsets_passing_that_filter(self):
        changesetsOnDefault = self.changesets[0:2] + self.changesets[3:4]
        self.assertEquals(changesetsOnDefault, filter_changesets(self.changesets, [on_default]))

    def test_two_filters_returns_changesets_passing_both(self):
        changesetsOnDefaultAndTDDed = self.changesets[:2]
        self.assertEquals(changesetsOnDefaultAndTDDed, filter_changesets(self.changesets, [is_tdded, on_default]))

    def test_three_filters_returns_changets_passing_all(self):
        changesetsOnDefaultAndTDDedSinceOct31980 = self.changesets[:1]
        self.assertEquals(changesetsOnDefaultAndTDDedSinceOct31980, filter_changesets(self.changesets, [is_tdded, on_default, after_date(OCT_3_1980_DATE)]))
