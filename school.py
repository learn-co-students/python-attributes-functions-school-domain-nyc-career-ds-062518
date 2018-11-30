class School:

    goose = "Duck, duck, mf."

    def __init__(self, name):
        self._name = name
        self._roster = {}

    def roster(self):
        return self._roster

    #decorators for _roster attribute

    # @property
    # def roster(self):
    #     return self._roster
    #
    # @roster.setter
    # def roster(self, roster):
    #     self._roster = roster

    def add_student(self, student_name, grade_level):
        if grade_level not in self._roster.keys():
            self._roster[grade_level] = []
            self._roster[grade_level].append(student_name)
        else:
            self._roster[grade_level].append(student_name)

    def grade(self, grade_level):
        return self._roster[grade_level]

    def sort_roster(self):
        for key in self._roster.keys():
            self._roster[key].sort()
            return self._roster


#we want to be able to add a key that is a grade
# we also want to be able to add a student to the student list, where the student list
#is the value paired with the key/grade
