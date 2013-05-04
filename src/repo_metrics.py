import os
import sys
from mercurial import hg, ui
from filters import IsTdded
from parse_arguments import parse_arguments
from fickle import Fickle

def get_count_and_percentage(base, my_filter):
    base_count = len(base)
    if base_count == 0:
        return 0, 0

    filtered_count = len(filter(my_filter, base))
    return filtered_count, float(filtered_count) / base_count * 100

def print_metric(base, metric_filter):
    print(metric_filter.print_result() % get_count_and_percentage(base, metric_filter))

def print_filters(filters):
    print('Filtering by...')
    for f in filters:
        print(f)
    print

def print_metrics(repo, base_filters, metrics_filters):
    if not repo.is_valid():
        print('There is no repository at %s' % os.getcwd())
        return

    if repo.is_empty():
        print('The repository is empty')
        return

    print_filters(base_filters)

    base = repo.filter_changesets(base_filters)

    if len(base) == 0:
        print('There are no changesets meeting the criteria')
        return

    print('Total Commits: %d' % len(base))

    for f in metrics_filters:
        print_metric(base, f)

def generate_and_display_metrics():
    repo = Fickle(os.getcwd())
    base_filters = parse_arguments(sys.argv)
    metrics_filters = [IsTdded()]
    print_metrics(repo, base_filters, metrics_filters)

if __name__ == '__main__':
    generate_and_display_metrics() 
