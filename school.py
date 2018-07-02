import copy

class School:
    def __init__(self, name):
        self._name = name
        self._roster = {}

    def roster(self):
        return self._roster

    def add_student(self, name, grade):
        if grade in self._roster.keys():
            self._roster[grade].append(name)
        else:
            self._roster[grade] = [name]
        return self._roster

    def grade(self, grade):
        return self._roster[grade]

    def sort_roster(self):
        sorted = copy.deepcopy(self._roster)
        for key in sorted:
            sorted[key].sort()
        return sorted
