import os
import shutil
import unittest
from mercurial import hg, ui
from test_support import Repository
from fickle import Fickle

class TestFickleIsEmpty(unittest.TestCase):
    def setUp(self):
        os.mkdir('repo')
        repo_dir = os.getcwd() + '/repo'
            
        self.repo = Repository(hg.repository(ui.ui(), repo_dir, create=True))
        self.fickle = Fickle(repo_dir)

    def tearDown(self):
        shutil.rmtree('repo')

    def test_repository_with_no_changesets_is_empty(self):
        self.assertTrue(self.fickle.is_empty())

    def test_repository_with_one_changeset_is_not_empty(self):
        self.repo.commit_files(['repo/testfile']) 
        self.assertFalse(self.fickle.is_empty())

