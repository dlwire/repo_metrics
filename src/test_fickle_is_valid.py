import os
import shutil
import unittest
from mercurial import hg, ui
from fickle import Fickle

class TestFickleIsValid(unittest.TestCase):
    def setUp(self):
        os.mkdir('repo')
        self.repo_dir = os.getcwd() + '/repo'

    def tearDown(self):
        shutil.rmtree('repo')

    def test_no_repository_is_not_valid(self):
        self.assertFalse(Fickle(self.repo_dir).is_valid())

    def test_repository_is_valid(self):
        hg.repository(ui.ui(), self.repo_dir, create=True)
        self.assertTrue(Fickle(self.repo_dir).is_valid())
