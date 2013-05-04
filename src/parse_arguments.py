from datetime import datetime
from filters import *
import argparse

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
