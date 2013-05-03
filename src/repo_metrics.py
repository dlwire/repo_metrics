import os
import sys
from mercurial import hg, ui
from filters import IsTdded, OnBranch
from parse_arguments import parse_arguments
from fickle import Fickle, filter_changesets2

def get_count_and_percentage(base, my_filter):
    base_count = len(base)
    if base_count == 0:
        return 0, 0

    filtered_count = len(filter(my_filter, base))
    return filtered_count, float(filtered_count) / base_count * 100

def print_tdded(base):
    print('Tested Commits: %d - %d percent' % get_count_and_percentage(base, IsTdded()))

def print_metrics(repo):
    if not repo.is_valid():
        print('There is no repository at %s' % os.getcwd())
        return
        
    if repo.is_empty():
        print('The repository is empty')
        return

    additional_filters = parse_arguments(sys.argv)

    base_filters = additional_filters + [OnBranch('default')]
    base = repo.filter_changesets(base_filters)

    if len(base) == 0:
        print('There are no changesets meeting the criteria')
        return

    print('Total Commits: %d' % len(base))
    print_tdded(base)

def generate_and_display_metrics():
    repo = Fickle(os.getcwd())
    print_metrics(repo)
    
if __name__ == '__main__':
    generate_and_display_metrics() 
