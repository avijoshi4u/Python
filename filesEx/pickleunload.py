import pickle

f = open("myStudent.txt", "rb")
obj = pickle.load(f)
obj.display()