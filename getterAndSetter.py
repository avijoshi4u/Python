class programmer:
    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setTechnologies(self, tech):
        self.technologies = tech

    def getTechnologies(self):
        return self.technologies


p1 = programmer()
p1.setName("John")
p1.setSalary("1000000")
p1.setTechnologies("Java,Python,VueJs")

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())