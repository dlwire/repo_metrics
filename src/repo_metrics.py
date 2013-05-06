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

def run_metric(base, metric_filter):
    total, percent = get_count_and_percentage(base, metric_filter)
    return metric_filter.label(), total, percent 

class DefaultOutput:
    def __init__(self):
        pass

    def output(self, base_filters, total, metric_label, metric_total, metric_percent):
        print('Filtering by...')
        for f in base_filters:
            print(f)
        print

        print('Total Commits: %d' % total)
        print('%s: %d - %d percent' % (metric_label, metric_total, metric_percent))

def print_metrics(repo, base_filters, metrics_filters, outputer):
    if not repo.is_valid():
        print('There is no repository at %s' % os.getcwd())
        return

    if repo.is_empty():
        print('The repository is empty')
        return

    base = repo.filter_changesets(base_filters)
    label, total, percent = run_metric(base, metrics_filters[0])
    outputer.output(base_filters, len(base), label, total, percent) 

def generate_and_display_metrics():
    repo = Fickle(os.getcwd())
    base_filters = parse_arguments(sys.argv)
    metrics_filters = [IsTdded()]
    print_metrics(repo, base_filters, metrics_filters, DefaultOutput())

if __name__ == '__main__':
    generate_and_display_metrics() 
