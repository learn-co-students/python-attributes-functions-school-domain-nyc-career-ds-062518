class School:
    
    def __init__(self, name):
        self._name = name
        self._roster = {}
        
#     @property    
#     def roster(self):
#         return self._roster
#    
#     @roster.setter
#     def roster(self, roster):
#         self._roster = roster
    def roster(self):
        return self._roster

    def add_student(self, name, grade_level):
        if grade_level not in self._roster.keys():
            self._roster[grade_level] = []
            self._roster[grade_level].append(name)
        else: 
            self._roster[grade_level].append(name)
            
    def grade(self, grade_level):
        return self._roster[grade_level]
    
    def sort_roster(self):
        for grade_level in self._roster.keys():
            self._roster[grade_level].sort()
        return self._roster

            