class Student:

    def __init__(self):
        # making the variable private using __
        self.__id = 123
        self.__name = "John"

    def disp(self):
        print(self.__id)
        print(self.__name)

s = Student()
#print(s.id)
s.disp()
# name mangling

print(s._Student__id)





