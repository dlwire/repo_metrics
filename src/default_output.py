from results import Results

class DefaultOutput:
    def __init__(self):
        pass

    def output(self, base_filters, result):
        print('Filtering by...')
        for f in base_filters:
            print(f)
        print

        print('Total Commits: %d' % result.total)
        print('%s: %d - %d percent' % (result.label, result.metric, result.percent))
