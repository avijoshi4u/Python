lst = [10, 20, "python", -10, 30, 50]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst * 4)
print(len(lst))

# Add and remove elements from the list
lst.append("Java")
lst.remove(-10)
del (lst[4])
print(lst)
lst.remove("Java")
lst.remove("python")

# To clear the list
# lst.clear()
# print(lst)
lst.append(-20)
lst.append(-30.99)
print(lst)
print("Max value is ", max(lst))
print("Min value is ", min(lst))

lst.insert(1, 99)
print(lst)

lst.sort()
print("After sorting", lst)
# to print in reverse order
lst.sort(reverse=True)
print("Reverse sorted order", lst)
print(lst.count(10))
print(lst.index(20))

# program

lst5 = [1, 1, 1, 1, 1, 2, 3, 3, 3, 4, 5, 6]
