lst = eval(input("Enter the list of elements"))
lst2 = []
for each_val in lst:
    if each_val not in lst2:
        lst2.append(each_val)
print(lst2)

s = set(lst)
print("set", s)
