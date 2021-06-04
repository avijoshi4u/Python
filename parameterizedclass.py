class course:

    def __init__(self, course_name, ratings):
        self.course_name = course_name
        self.ratings = ratings

    def average(self):
        numberOfRatings = len(self.ratings)
        average = sum(self.ratings) / numberOfRatings
        print("Average of ", self.course_name, "is ", average)


c1 = course("Java", [1, 2, 3, 4, 5])
print(c1.course_name)
print(c1.ratings)
c1.average()

c2 = course("Java web service", [5, 5, 5, 5, 5])
print(c2.course_name)
print(c2.ratings)
c2.average()
