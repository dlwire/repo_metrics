class Changeset:
    def __init__(self, filepaths=[], branch='default'):
        self.filepaths = filepaths
        self.branchName = branch

    def files(self):
        return self.filepaths

    def branch(self):
        return self.branchName
