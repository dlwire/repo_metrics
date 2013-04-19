import os
import unittest
import shutil
from mercurial import hg, ui
from repo_metrics import repository_exists

class TestRepositoryExists(unittest.TestCase):
    def setUp(self):
        os.mkdir('repo')
    
    def tearDown(self):
        shutil.rmtree('repo')

    def test_no_repository_is_false(self):
        self.assertFalse(repository_exists(os.getcwd() + '/repo'))

    def test_repository_present_is_true(self):
        hg.repository(ui.ui(), os.getcwd() + '/repo', True)
        self.assertTrue(repository_exists(os.getcwd() + '/repo'))

if __name__ == '__main__':
    unittest.main()
