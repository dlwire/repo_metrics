from datetime import datetime
from filters import after_date, by_user
import argparse

def parse_arguments(arguments):
    if len(arguments) == 1:
        return []

    p = argparse.ArgumentParser()
    p.add_argument('--afterDate', type=parse_date, nargs='?')
    p.add_argument('--users', type=lambda x: x, nargs='*')
    p.add_argument('args', nargs=argparse.REMAINDER)
    print "Found arguments: " + str(arguments)
    args = p.parse_args(arguments[1:])

    filters = []
    if args.afterDate:
        filters.append(after_date(args.afterDate))
    if args.users:
        filters.append(by_user(args.users))

    return filters

def parse_date(date):
    print "Date found: " + str(date)
    year, month, day = date.split('-')

    return datetime(int(year), int(month), int(day))
