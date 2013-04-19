import os
import shutil
import unittest
from mercurial import commands, hg, ui
from repo_metrics import get_changesets

def len_generator(my_generator):
    return sum(1 for _ in my_generator)

class TestGetChangesets(unittest.TestCase):
    def setUp(self):
        os.mkdir('repo')
        self.repo_path = os.getcwd() + '/repo'
        self.repo = hg.repository(ui.ui(), self.repo_path, True)
    
    def tearDown(self):
        shutil.rmtree('repo')

    def commit_file(self, filename, comment):
        filepath = self.repo_path + '/' + filename
        with open(filepath, 'w') as f:
            f.writelines('content')
        commands.add(ui.ui(), self.repo, filepath)
        commands.commit(ui.ui(), self.repo, message=comment, user='dont care')

    def test_empty_repository_returns_generator_with_0_changesets(self):
        self.assertEqual(0, len_generator(get_changesets(self.repo)))

    def test_repository_with_one_changeset_returns_the_changeset(self):
        self.commit_file('first_file', 'first commit')

        self.assertEqual(1, len_generator(get_changesets(self.repo)))

    def test_repository_with_two_changesets_returns_two_changesets(self):
        self.commit_file('first_file', 'first commit')
        self.commit_file('second_file', 'second commit')

        self.assertEqual(2, len_generator(get_changesets(self.repo)))

    def test_changesets_are_returned_in_commit_order(self):
        self.commit_file('first_file', 'first commit')
        self.commit_file('second_file', 'second commit')
        
        changesets = get_changesets(self.repo)
        self.assertEqual('first commit', changesets.next().description())
        self.assertEqual('second commit', changesets.next().description())


if __name__ == '__main__':
    unittest.main()
