def is_tdded(changeset):
    return any(['test' in filename.lower() for filename in changeset.files()])
    
def on_default(changeset):
    return 'default' == changeset.branch()
