from datetime import datetime
from filters import after_date, by_user

def parse_arguments(arguments):
    if len(arguments) == 1:
        return []

    filters = []
    for argument in arguments[1:]:
        if '-afterDate' in argument:
            filters.append(after_date(parse_date(argument)))
        else:
            filters.append(by_user(parse_user(argument)))

    return filters

def parse_date(dateArgument):
    date = dateArgument.strip("-afterDate").strip("'")
    year, month, day = date.split('-')

    return datetime(int(year), int(month), int(day))

def parse_user(userArgument):
    return [token.strip() for token in userArgument.strip("-user").strip("'").split(',')]

