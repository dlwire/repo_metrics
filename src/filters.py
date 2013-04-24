from datetime import datetime

def is_tdded(changeset):
    return any(['test' in filename.lower() for filename in changeset.files()])
    
def on_default(changeset):
    return 'default' == changeset.branch()

def after_date(date):
    return lambda changeset: date < datetime.fromtimestamp(changeset.date()[0])

def by_user(user):
    return lambda changeset: user == changeset.user()
