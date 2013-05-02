import os
import sys
from mercurial import hg, ui
from filters import after_date, is_tdded, on_default
from parse_arguments import parse_arguments
from fickle import Fickle

def len_generator(generator):
    return sum(1 for _ in generator)

def get_commit_percent(repo, numerator_filters, denominator_filters):
    numerator_count = len_generator(repo.filter_changesets(numerator_filters))
    denominator_count = max(1, len_generator(repo.filter_changesets(denominator_filters)))

    return float(numerator_count) / denominator_count * 100

def print_metrics(repo):
    if repo.is_empty():
        print('The repository is empty')
        return

    additional_filters = parse_arguments(sys.argv)

    numerator_filters = additional_filters + [on_default, is_tdded]
    denominator_filters = additional_filters + [on_default]

    if len_generator(repo.filter_changesets(denominator_filters)) == 0:
        print('There are no changesets meeting the criteria')
        return
        
    percentage = get_commit_percent(repo, numerator_filters, denominator_filters)

    print('%d percent of commits have tests' % percentage)

def generate_and_display_metrics():
    repo = Fickle(os.getcwd())
    if not repo.is_valid():
        print('There is no repository at %s' % os.getcwd())
        return
    
    print_metrics(repo)
    
if __name__ == '__main__':
    generate_and_display_metrics() 
