import time
from mercurial import commands, hg, ui

class Changeset:
    def __init__(self, filepaths=[], branch='default', epochTime=time.time(), user="Don't Care"):
        self.myFiles = filepaths
        self.myBranch = branch
        self.myDate = epochTime
        self.myUser = user

    def files(self):
        return self.myFiles

    def branch(self):
        return self.myBranch

    def date(self):
        return (self.myDate, 1231)

    def user(self):
        return self.myUser

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
        commands.commit(ui.ui(), self.repo, message="Don't Care", user='Testy McTesterson', addremove=False, logfile=None, date=None)

    def create_branch(self, branchName):
        commands.branch(ui.ui(), self.repo, branchName)

    def get_repo(self):
        return self.repo

class ParsedArgumentsMock:
    def __init__(self, afterDate=None, users=None, extensions=None, branch='default'):
        self.afterDate = afterDate
        self.users = users
        self.extensions = extensions
        self.branch = branch

