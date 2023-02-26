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
   
  def __init__(self):
    super().__init__("Teacher")
   
  def work(self):
    self.salary += 2500

student = Student()
teacher = Teacher()
student.study()
print(student.grade)
teacher.work()
print(teacher.work)

