dict1 = {1: "John", 2: "Bob", 3: "Gill"}
print(type(dict1))

print(dict.get())

print(dict1.items())

print("All keys are:")
k = dict1.keys()
for i in k:
    print(i)

v = dict1.values()
print("All values are:")
for i in v:
    print(i)

print(dict1[3])

del (dict1[2])
print(dict1)

student = {"John": {"Maths", "English", "Phy"}, "Bob": {"English", "Phy"}, "Jim": {"Maths"}}
keys = student.keys()
for key in keys:
    print("courses taken by", key, "are:")
    for eachcourse in student[key]:
        print(eachcourse)
