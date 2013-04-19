from datetime import datetime
from filters import after_date

def parse_arguments(arguments):
    if len(arguments) == 1:
        return []

    after_date_filter = after_date(parse_date(arguments[1]))
    return [after_date_filter]

def parse_date(date):
    year, month, day = date.split('-')
    return datetime(int(year), int(month), int(day))
