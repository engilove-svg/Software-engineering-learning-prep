class Student:
    def __init__(self,grade):
        self._grade=grade

    @property 
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,value):
        if value>100 and value<=0:
            print("Invalid value.")
        else:
            self._grade=value

student = Student(80)

student.grade = 95
print(student.grade)