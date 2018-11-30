class School:
    def __init__(self, name):
        self._name = name
        self._roster = {}


    def roster(self):
        return self._roster

    def add_student(self, name, grade):
        if grade not in self._roster.keys():
            self._roster[grade] = []
        self._roster[grade].append(name)
    def grade(self, grade):
        return self._roster[grade]

    def sort_roster(self):
        for grade in self._roster.keys():
            self._roster[grade] = sorted(self._roster[grade])
        return self._roster
