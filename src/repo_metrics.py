import os
import sys
from mercurial import hg, ui

def get_count_and_percentage(base, my_filter):
    base_count = len(base)
    if base_count == 0:
        return 0, 0

    filtered_count = len(filter(my_filter, base))
    return filtered_count, float(filtered_count) / base_count * 100

def run_metric(base, metric_filter):
    total, percent = get_count_and_percentage(base, metric_filter)
    return metric_filter.label(), total, percent 

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
