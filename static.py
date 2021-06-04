class Student:
    major = "CSE"

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("John", 23)
s2 = Student("Harry", 30)
print(s1.major)
print(s2.major)
print(Student.major)
