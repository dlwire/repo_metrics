import argparse
import os
import sys
from datetime import datetime
from default_output import DefaultOutput
from monthly_output import MonthlyOutput
from fickle import Fickle
from filters import *
from repo_metrics import *

def get_filters_from_args(parsed_arguments):
    filters = []

    if parsed_arguments.afterDate:
        after_date = AfterDate(parsed_arguments.afterDate)
        filters.append(after_date)

    if parsed_arguments.users:
        by_users = ByUsers(parsed_arguments.users)
        filters.append(by_users)

    if parsed_arguments.extensions:
        by_extensions = ByExtensions(parsed_arguments.extensions)
        filters.append(by_extensions)

    filters.append(OnBranch(parsed_arguments.branch))

    return filters

def parse_arguments(arguments):
    p = argparse.ArgumentParser()
    p.add_argument('--afterDate', type=datetime_from_string, nargs='?')
    p.add_argument('--users', type=lambda x: x, nargs='*')
    p.add_argument('--extensions', type=lambda x: x, nargs='*')
    p.add_argument('--branch', type=lambda x: x, default='default', nargs='?')
    p.add_argument('--byMonth', action='store_true', default=False)
    p.add_argument('args', nargs=argparse.REMAINDER)
    args = p.parse_args(arguments[1:])

    return args

def datetime_from_string(date):
    year, month, day = date.split('-')
    return datetime(int(year), int(month), int(day))

def generate_and_display_metrics():
    repo = Fickle(os.getcwd())
    args = parse_arguments(sys.argv)
    base_filters = get_filters_from_args(args)
    metrics_filter = IsTdded()

    if not args.byMonth:
        print_metrics(repo, base_filters, metrics_filter, DefaultOutput())
    else:
        monthly_metrics(repo, base_filters, metrics_filter, MonthlyOutput())

if __name__ == '__main__':
    generate_and_display_metrics() 
