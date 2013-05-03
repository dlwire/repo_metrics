from datetime import datetime
from filters import after_date, by_user, by_extension
import argparse

def parse_arguments(arguments):
    if len(arguments) == 1:
        return []

    p = argparse.ArgumentParser()
    p.add_argument('--afterDate', type=parse_date, nargs='?')
    p.add_argument('--users', type=lambda x: x, nargs='*')
    p.add_argument('--extensions', type=lambda x: x, nargs='*')
    p.add_argument('args', nargs=argparse.REMAINDER)
    args = p.parse_args(arguments[1:])

    filters = []

    filteringBy = ['Filtering by...']
    if args.afterDate:
        filteringBy.append('    After Date: ' + args.afterDate.isoformat().split('T')[0])
        filters.append(after_date(args.afterDate))

    if args.users:
        filteringBy.append('    Users: ' + ', '.join(args.users))
        filters.append(by_user(args.users))

    if args.extensions:
        filteringBy.append('    Extensions: ' + ', '.join(args.extensions))
        filters.append(by_extension(args.extensions))

    if len(filteringBy) > 1:
        print('\n'.join(filteringBy))
        print

    return filters

def parse_date(date):
    year, month, day = date.split('-')
    return datetime(int(year), int(month), int(day))
