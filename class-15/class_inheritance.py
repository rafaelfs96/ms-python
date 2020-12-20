
class Person:
  def __init__(self, name):
    self.name = name

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value

  def say_hello(self):
    print(self.name)

class Student(Person):
  def __init__(self, name, school):
    super().__init__(name)
    self.school = school
  
  def sing_school(self):
    print(self.school)

student = Student('rafael', 'senac')
student.name = 'Rafael'
student.say_hello()
student.sing_school()

print(isinstance(student, Student)) # is student an instance of Studant
print(isinstance(student, Person)) # is student an instance of Person
print(issubclass(Student, Person)) # is Student a subclass of Person