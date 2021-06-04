class ObjectCounter:
    noOfObject = 0

    def __init__(self):
        ObjectCounter.noOfObject+=1

    @staticmethod
    def display():
        print(ObjectCounter.noOfObject)



c1 = ObjectCounter()
c2 = ObjectCounter()

c2.display()
ObjectCounter.display()