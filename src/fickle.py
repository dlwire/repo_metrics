from mercurial import hg, ui

class Fickle:
    def __init__(self, path):
        try:
            self.repo = hg.repository(ui.ui(), path)
        except:
            self.repo = []
        
    def is_valid(self):
        return self.repo != []

    def is_empty(self):
        return len(self.repo) == 0

    def changesets(self):
        return (self.repo[revisionNumber] for revisionNumber in range(0, len(self.repo)))

    def filter_changesets(self, filters):
        if len(filters) == 0: 
            return self.changesets()
        return filter(filters[0], self.filter_changesets(filters[1:]))

