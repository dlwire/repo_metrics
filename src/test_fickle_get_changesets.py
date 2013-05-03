import os
import shutil
import unittest
from mercurial import hg, ui
from test_support import Repository
from fickle import Fickle

def len_generator(my_generator):
    return sum(1 for _ in my_generator)

class TestGetChangesets(unittest.TestCase):
    def setUp(self):
        os.mkdir('repo')
        self.repo_path = os.getcwd() + '/repo'
        self.repo = Repository(hg.repository(ui.ui(), self.repo_path, True))
        self.fickle = Fickle(os.getcwd() + '/repo')
    
    def tearDown(self):
        shutil.rmtree('repo')

    def test_empty_repository_returns_generator_with_0_changesets(self):
        self.assertEqual(0, len_generator(self.fickle.changesets()))

    def test_repository_with_one_changeset_returns_the_changeset(self):
        self.repo.commit_files(['repo/first_file'])

        self.assertEqual(1, len_generator(self.fickle.changesets()))

    def test_repository_with_two_changesets_returns_two_changesets(self):
        self.repo.commit_files(['repo/first_file'])
        self.repo.commit_files(['repo/second_file'])

        self.assertEqual(2, len_generator(self.fickle.changesets()))

    def test_changesets_are_returned_in_commit_order(self):
        self.repo.commit_files(['repo/first_file'])
        self.repo.commit_files(['repo/second_file'])
        
        changesets = self.fickle.changesets()
        self.assertEqual(['first_file'], changesets.next().files())
        self.assertEqual(['second_file'], changesets.next().files())

if __name__ == '__main__':
    unittest.main()
