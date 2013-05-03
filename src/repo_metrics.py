import os
import sys
from mercurial import hg, ui
from filters import after_date, is_tdded, on_default
from parse_arguments import parse_arguments
from fickle import Fickle, filter_changesets2

def len_generator(generator):
    return sum(1 for _ in generator)

def get_commit_percent(repo, numerator_filters, denominator_filters):
    changesets = filter_changesets2(repo.changesets(), denominator_filters)
    denominator_count = len_generator(changesets)
    numerator_count = len_generator(filter_changesets2(changesets, numerator_filters))

    percent = 0
    if denominator_count != 0:
        percent = float(numerator_count) / denominator_count * 100

    return (percent, numerator_count, denominator_count)

def print_tdded(base):
    tdded = filter(is_tdded, base)

    percentage = float(len(tdded)) / len(base) * 100

    print('Tested Commits: %d - %d percent' % (len(tdded), percentage))

def print_metrics(repo):
    if not repo.is_valid():
        print('There is no repository at %s' % os.getcwd())
        return
        
    if repo.is_empty():
        print('The repository is empty')
        return

    additional_filters = parse_arguments(sys.argv)

    base_filters = additional_filters + [on_default]
    base = filter_changesets2(repo.changesets(), base_filters)

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
