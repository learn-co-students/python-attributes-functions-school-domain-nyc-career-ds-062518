class School:



   def __init__(self, name):
       self._name = name
       self._roster = {}

   def roster(self):
       return self._roster




   def add_student(self, name, grade):
       self._grade= grade
       self._name = name
       if self._grade not in self._roster.keys():
           self._roster[self._grade]=[self._name]
       else:
           self._roster[self._grade].append(self._name)
       return self._roster

   def grade (self,grade):
      return self._roster[grade]

   def sort_roster(self):
      for grade  in self._roster.keys() :
         self._roster[grade]= sorted(self._roster[grade])
      return self._roster
