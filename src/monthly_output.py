from results import Results

class MonthlyOutput:
    def __init__(self):
        pass

    def header(self, base_filters):
        print('Filtering by...')
        for f in base_filters:
            print(f)
        print
        print 'YYYY-MM, Total Commits, Tested Commits, % Tested'

    def body(self, month, result):
        print('%s, %d, %d, %d' % (month, result.total, result.metric, result.percent))
