#2-m
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def study(self):
        print("I am studying")
        
    def take_exam(self):
        print("I am taking exam")
        

class Student(Person):
    def __init__(self, grade):
        self._grade = grade
        
    
u1 = Person("John", 22)
u1.study()
u1.take_exam()
