import os
import shutil
import unittest
from mercurial import commands, hg, ui
from repo_metrics import get_tdded_commit_percentage

def len_generator(my_generator):
    return sum(1 for _ in my_generator)

class TestGetTestCommitPercentage(unittest.TestCase):
    def setUp(self):
        os.mkdir('repo')
        self.repo_path = os.getcwd() + '/repo'
        self.repo = hg.repository(ui.ui(), self.repo_path, True)
    
    def tearDown(self):
        shutil.rmtree('repo')

    def commit_file(self, filename):
        filepath = self.repo_path + '/' + filename
        with open(filepath, 'w') as f:
            f.writelines('content')
        commands.add(ui.ui(), self.repo, filepath)
        commands.commit(ui.ui(), self.repo, message='dont care', user='dont care')

    def test_0_commits_is_0_percent_tdded(self):
        self.assertEqual(0, get_tdded_commit_percentage(self.repo))

    def test_1_code_only_commit_is_0_percent_tdded(self):
        self.commit_file('only_code.cpp')

        self.assertEqual(0, get_tdded_commit_percentage(self.repo))

    def test_1_test_only_commit_is_100_percent_tdded(self):
        self.commit_file('only_test.cpp')
        
        self.assertEqual(100, get_tdded_commit_percentage(self.repo))

    def test_1_test_commit_and_1_code_commit_is_50_percent_tdded(self):
        self.commit_file('only_code.cpp')
        self.commit_file('only_test.cpp')

        self.assertEqual(50, get_tdded_commit_percentage(self.repo))
       
if __name__ == '__main__':
    unittest.main()
