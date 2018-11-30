class School:

    def __init__(self, name):
        self._roster = {}
        self._name = name


    def roster(self):
        return self._roster

    def add_student(self, name, grade):
        if grade in self._roster:
            self._roster[grade].append(name)
        else:
            self._roster[grade] = [name]

    def grade(self, grade):
        return self._roster[grade]

    def sort_roster(self):
        for grade, names in self._roster.items():
            self._roster[grade] = sorted(names)
        return self._roster
