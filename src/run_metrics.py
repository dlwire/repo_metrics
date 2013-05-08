import argparse
import os
import sys
from datetime import datetime
from default_output import DefaultOutput
from fickle import Fickle
from filters import *
from repo_metrics import print_metrics

def parse_arguments(arguments):
    p = argparse.ArgumentParser()
    p.add_argument('--afterDate', type=parse_date, nargs='?')
    p.add_argument('--users', type=lambda x: x, nargs='*')
    p.add_argument('--extensions', type=lambda x: x, nargs='*')
    p.add_argument('--branch', type=lambda x: x, default='default', nargs='?')
    p.add_argument('args', nargs=argparse.REMAINDER)
    args = p.parse_args(arguments[1:])

    filters = []

    if args.afterDate:
        after_date = AfterDate(args.afterDate)
        filters.append(after_date)

    if args.users:
        by_users = ByUsers(args.users)
        filters.append(by_users)

    if args.extensions:
        by_extensions = ByExtensions(args.extensions)
        filters.append(by_extensions)

    filters.append(OnBranch(args.branch))

    return filters

def parse_date(date):
    year, month, day = date.split('-')
    return datetime(int(year), int(month), int(day))

def generate_and_display_metrics():
    repo = Fickle(os.getcwd())
    base_filters = parse_arguments(sys.argv)
    metrics_filters = [IsTdded()]
    print_metrics(repo, base_filters, metrics_filters, DefaultOutput())

if __name__ == '__main__':
    generate_and_display_metrics() 
