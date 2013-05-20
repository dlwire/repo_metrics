import unittest
from test_support import Changeset
from group_by_month import group_by_month

OCT_1980_EPOCH = 339310800
NOV_1980_EPOCH = 341989200

class TestGroupByMonth(unittest.TestCase):
    def test_no_changesets(self):
        monthly = group_by_month([])
        months = []
        changes = []
        for k, g in monthly:
            months.append(k)
            changes.append(list(g))

        self.assertEquals(0, len(months))
        self.assertEquals(0, len(changes))

    def test_1_changeset_1_group(self):
        changesets = [Changeset(epochTime=OCT_1980_EPOCH)]

        monthly = group_by_month(changesets)
        months = []
        changes = []
        for k, g in monthly:
            months.append(k)
            changes.append(list(g))

        self.assertEquals(1, len(months))
        self.assertEquals('1980-10', months[0])
        self.assertEquals(1, len(changes))

    def test_2_changesets_in_2_months(self):
        changesets = [Changeset(epochTime=OCT_1980_EPOCH), Changeset(epochTime=NOV_1980_EPOCH)]

        monthly = group_by_month(changesets)
        months = []
        changes = []
        for k, g in monthly:
            months.append(k)
            changes.append(list(g))

        self.assertEquals(2, len(months))
        self.assertEquals('1980-10', months[0])
        self.assertEquals('1980-11', months[1])
        
        self.assertEquals(2, len(changes))
        self.assertEquals(1, len(changes[0]))
        self.assertEquals(1, len(changes[1]))


if __name__ == '__main__':
    unittest.main()
