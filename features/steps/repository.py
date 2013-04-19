# -*- coding: utf-8 -*-
from lettuce import step, world
from os import mkdir
from mercurial import commands, hg, ui

class Repository:
    def __init__(self, repo):   
        self.repo = repo

    def add_file(self, filepath):
        with open(filepath, 'w') as f:
            f.writelines("Don't Care")
        commands.add(ui.ui(), self.repo, filepath)

    def commit_files(self, filepaths, myDate=None):
        for f in filepaths:
            self.add_file(f)
        commands.commit(ui.ui(), self.repo, message="Don't Care", user='Testy McTesterson', addremove=False, logfile=None, date=myDate)

    def create_branch(self, branchName):
        commands.branch(ui.ui(), self.repo, branchName)

def create_repository():
    world.repo = Repository(hg.repository(ui.ui(), world.REPO_DIR, create=True))

@step(u'an empty repository')
def a_repository_with_0_changesets(step):
    create_repository()

@step(u'a repository with changesets$')
def a_repository_with_changesets(step):
    create_repository()

    world.repo.commit_files(['repo/codefile', 'repo/codefiltest'])
    world.repo.commit_files(['repo/second_codefile'])

@step(u'a repository with changesets to multiple branches')
def a_repository_with_changesets_to_multiple_branches(step):
    create_repository()

    world.repo.commit_files(['repo/codefile', 'repo/codefiltest'])
    world.repo.commit_files(['repo/second_codefile'])

    world.repo.create_branch("Don't Care")

    world.repo.commit_files(['repo/third_codefile'])
    world.repo.commit_files(['repo/second_testfile'])

@step(u'a repository with changesets before the start date')
def a_repository_with_changesets_before_the_start_date(step):
    create_repository()

    world.repo.commit_files(['repo/codefile', 'repo/codefiletest'], '1980-10-02')

@step(u'a repository with changesets before and after the start date')
def a_repository_with_changesets_before_and_after_the_start_date(step):
    create_repository()

    world.repo.commit_files(['repo/codefile1', 'repo/codefiletest'], '1980-10-02')
    world.repo.commit_files(['repo/testfile'])
    world.repo.commit_files(['repo/codefile2'])
