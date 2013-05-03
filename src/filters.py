from datetime import datetime

class IsTdded:
    def __init__(self):
        pass
        
    def __call__(self, changeset):
        return any(['test' in filename.lower() for filename in changeset.files()])

class OnBranch:
    def __init__(self, branch):
        self.branch = branch

    def __call__(self, changeset):
        return self.branch == changeset.branch()

class AfterDate:
    def __init__(self, date):
        self.date = date

    def __call__(self, changeset):
        return self.date < datetime.fromtimestamp(changeset.date()[0])

    def __str__(self):
        return 'After Date: ' + self.date.isoformat().split('T')[0]

class ByUsers:
    def __init__(self, users):
        self.users = users

    def __call__(self, changeset):
        return any([user.lower() in changeset.user().lower() for user in self.users])

    def __str__(self):
        return 'Users: ' + ', '.join(self.users)

class ByExtensions:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, changeset):
        return any([file.lower().endswith('.' + extension) for extension in self.extensions for file in changeset.files()])

    def __str__(self):
        return 'Extensions: ' + ', '.join(self.extensions)
