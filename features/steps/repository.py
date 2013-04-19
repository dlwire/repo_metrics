# -*- coding: utf-8 -*-
from lettuce import step, world
from os import mkdir
from mercurial import commands, hg, ui

def add_file(filepath):
    with open(filepath, 'w') as f:
        f.writelines('Dont Care')
    commands.add(ui.ui(), world.repo, filepath)

def commit_files(filenames, myDate=None):
    for f in filenames:
        add_file(f)
    commands.commit(ui.ui(), world.repo, message='dont care', user='Testy McTesterson', addremove=False, logfile=None, date=None)

def create_repository():
    world.repo = hg.repository(ui.ui(), world.REPO_DIR, create=True)

@step(u'an empty repository')
def a_repository_with_0_changesets(step):
    create_repository()

@step(u'a repository with changesets$')
def a_repository_with_changesets(step):
    create_repository()

    commit_files(['repo/codefile', 'repo/codefiltest'])
    commit_files(['repo/second_codefile'])

@step(u'a repository with changesets to multiple branches')
def a_repository_with_changesets_to_multiple_branches(step):
    create_repository()

    commit_files(['repo/codefile', 'repo/codefiltest'])
    commit_files(['repo/second_codefile'])

    commands.branch(ui.ui(), world.repo, 'dont care')

    commit_files(['repo/third_codefile'])
    commit_files(['repo/second_testfile'])

@step(u'Given a repository with changesets before the start date')
def given_a_repository_with_changesets_before_the_start_date(step):
    create_repository()

    commit_files(['repo/codefile', 'repo/codefiletest'], '1980-10-02')
