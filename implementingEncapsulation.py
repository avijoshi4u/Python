# Implementing Encapsulation
class Student:

    def setId(self, sid):
        self.sid = sid

    def getId(self):
        return self.sid

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


s = Student()
s.setId(1)
s.setName("John")
print(s.getId())
print(s.getName())

