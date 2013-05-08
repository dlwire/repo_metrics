class DefaultOutput:
    def __init__(self):
        pass

    def output(self, base_filters, total, metric_label, metric_total, metric_percent):
        print('Filtering by...')
        for f in base_filters:
            print(f)
        print

        print('Total Commits: %d' % total)
        print('%s: %d - %d percent' % (metric_label, metric_total, metric_percent))

