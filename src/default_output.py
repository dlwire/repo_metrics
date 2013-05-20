from results import Results

class DefaultOutput:
    def __init__(self):
        pass

    def header(self, base_filters):
        print('Filtering by...')
        for f in base_filters:
            print(f)
        print

    def body(self, result):
        print('Total Commits: %d' % result.total)
        print('%s: %d - %d percent' % (result.label, result.metric, result.percent))
