class School:
    def __init__ (self, name, roster = {}, student_list = []):
        self._name = name
        self._roster = roster
        self._student_list = student_list

    def roster(self):
        return self._roster

    def add_student(self, student, grade):
        if grade not in self._roster.keys():
            self._roster[grade] = []
        self._roster[grade].append(student)

    def grade(self, grade):
        return self._roster[grade]

    def sort_roster(self):
        for students in self._roster.values():
            students.sort()
        return self._roster
