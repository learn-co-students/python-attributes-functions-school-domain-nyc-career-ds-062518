class School:
    def __init__(self, name):
        self._name = name
        self._roster = {}

    def roster(self):
        return self._roster

    def add_student(self, name, grade):
        if grade in self.roster():
            self.roster()[grade].append(name)
        else:
            self.roster()[grade] = [name]

    def grade(self, grade):
        return self.roster()[grade]

    def sort_roster(self):
        for key in self.roster().keys():
            self.roster()[key] = self.roster()[key].sort()
        return self.roster()
