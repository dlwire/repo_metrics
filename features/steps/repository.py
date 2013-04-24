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

    def commit_files(self, filepaths, commitDate=None, commitUser="Don't Care"):
        for f in filepaths:
            self.add_file(f)
        commands.commit(ui.ui(), self.repo, message="Don't Care", user=commitUser, addremove=False, logfile=None, date=commitDate)

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

    world.repo.commit_files(['repo/codefile', 'repo/codefiletest'], commitDate='1980-10-02')

@step(u'a repository with changesets before and after the start date')
def a_repository_with_changesets_before_and_after_the_start_date(step):
    create_repository()

    world.repo.commit_files(['repo/codefile1', 'repo/codefiletest'], commitDate='1980-10-02')
    world.repo.commit_files(['repo/testfile'])
    world.repo.commit_files(['repo/codefile2'])

@step(u'a repository with no changesets commited by the user')
def a_repository_with_no_changesets_commited_by_the_user(step):
    create_repository()
    
    world.repo.commit_files(['repo/codefile'], commitUser='Another User')

@step(u'a repository with changesets committed by a user')
def a_repository_with_changesets_committed_by_a_user(step):
    create_repository()

    world.repo.commit_files(['repo/codefile1', 'repo/codefiletest'], commitUser='Another User')
    world.repo.commit_files(['repo/testfile'], commitUser='A User')
    world.repo.commit_files(['repo/codefile2'], commitUser='A User')
