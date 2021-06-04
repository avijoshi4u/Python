"""s= input()
print(s)
name=input("Please enter the name")
print(name)

i = int(input("Enter the value of i"))
print(type(i))
print("Value of i",i)

j = input("Enter the value of j")
print(type(j))
print("Value of j",j)"""

lst=[x for x in input("Enter three number separated by spaces").split()]
print(lst)

lst1=[int(x) for x in input("Enter three number separated by spaces").split()]
print(lst1)

lst2=[float(x) for x in input("Enter three number separated by comma").split(",")]
print(lst2)
