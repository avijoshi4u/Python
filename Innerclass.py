class Car:

    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number

        def disp(self):
            print("engine started")


c = Car("BMW", 2021)
e = c.Engine(10)
e.disp()
