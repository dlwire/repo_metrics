from datetime import datetime
from filters import after_date, by_user

def parse_arguments(arguments):
    if len(arguments) == 1:
        return []

    filters = []
    if "-afterDate'" in arguments[1]:
        filters.append(after_date(parse_date(arguments[1])))
    else:   
        filters.append(by_user(parse_user(arguments[1])))

    return filters

def parse_date(dateArgument):
    date = dateArgument.strip("-afterDate").strip("'")
    year, month, day = date.split('-')

    return datetime(int(year), int(month), int(day))

def parse_user(userArgument):
    return userArgument.strip("-user").strip("'")
