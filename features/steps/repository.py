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

    for changeset_dict in step.hashes:
        files = [world.REPO_DIR + '/' + filename.strip() for filename in changeset_dict['files'].split(',')]

        if 'branch' in changeset_dict.keys():
            world.repo.create_branch(changeset_dict['branch'])

        date = None
        if 'date' in changeset_dict.keys():
            date = changeset_dict['date'].strip()

        user = 'Default User'
        if 'user' in changeset_dict.keys():
            user = changeset_dict['user'].strip()
            
        world.repo.commit_files(files, commitDate=date, commitUser=user)

