import os
import sys
from math import floor
from mercurial import hg, ui
from group_by_month import group_by_month
from results import Results

def convert_to_percent(numerator, denominator):
    return floor(float(numerator) / denominator * 100)

def run_metric(base, metric_filter):
    total = len(base)
    if total == 0:
        return Results(0, '', 0, 0)

    metric = len(filter(metric_filter, base))
    
    return Results(total, metric_filter.label(), metric, convert_to_percent(metric, total))

def print_metrics(repo, base_filters, metrics_filter, outputer):
    if not repo.is_valid():
        print('There is no repository at %s' % os.getcwd())
        return

    if repo.is_empty():
        print('The repository is empty')
        return

    outputer.header(base_filters)

    base = repo.filter_changesets(base_filters)
    result = run_metric(base, metrics_filter)
    outputer.body(result) 

def monthly_metrics(repo, base_filters, metrics_filter, outputer):
    if not repo.is_valid():
        print('There is no repository at %s' % os.getcwd())
        return

    if repo.is_empty():
        print('The repository is empty')
        return

    outputer.header(base_filters)

    base = repo.filter_changesets(base_filters)
    monthly = group_by_month(base)
    for k, g in monthly:
        result = run_metric(list(g), metrics_filter)
        outputer.body(k, result)

    
