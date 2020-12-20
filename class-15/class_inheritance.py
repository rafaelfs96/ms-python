
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

  # override say_hello method
  # OBS: super().say_hello() calls the parent method, and it is optional to call it
  def say_hello(self):
    super().say_hello()
    print(f'hey')

  # __str__ is optional, use it only when you need to
  def __str__(self):
    return f'{self.name} attends {self.school}'

student = Student('rafael', 'Senac')
student.name = 'Rafael'
student.say_hello()
student.sing_school()

print(student)

print(f'is student an instance of Student? {isinstance(student, Student)}')
print(f'is student an instance of Person? {isinstance(student, Person)}')
print(f'is Student a subclass of Person? {issubclass(Student, Person)}')