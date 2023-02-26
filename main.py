class Person:
    def __init__(self, name):
      self.name = name
class Student(Person):
  grade = 0
  def study(self):
    self.grade += 2

  def __init__(self):
    super().__init__("Student")

class Teacher(Person):
  salary = 0
  student = []

student = Student()
student.study()
print(student.grade)

