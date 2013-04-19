import os
from mercurial import hg, ui
from filters import is_tdded, on_default

def len_generator(generator):
    return sum(1 for _ in generator)

def repository_exists(directory):
    try:
        hg.repository(ui.ui(), directory)
        return True
    except:
        return False

def get_changesets(repo, filters=[]):
    if len(filters) == 0:
        return (repo[revNum] for revNum in range(0, len(repo)))
    return filter(filters[0], get_changesets(repo, filters[1:]))

def get_tdded_commit_percentage(repo):
    changeset_count = max(1, len_generator(get_changesets(repo, [on_default])))
    tdded_count = len_generator(get_changesets(repo, [on_default, is_tdded]))

    return float(tdded_count) / changeset_count * 100

def print_test_commit_percentage(): 
    if repository_exists(os.getcwd()):
        repo = hg.repository(ui.ui(), os.getcwd())

        if len(repo) != 0:
            print('%d percent of commits have tests' % get_tdded_commit_percentage(repo))
        else:
            print('The repository is empty')
    else:
        print('There is no repository at %s' % os.getcwd())

if __name__ == '__main__':
    print_test_commit_percentage() 
