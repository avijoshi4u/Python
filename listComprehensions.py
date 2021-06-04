'''list comprehensions are a shortcut  to create a one list
out of another by applying the logic we want on the first list as well as  we can apply
conditions on the right hand side only if the condition is satisfied that item will be included in the resulting list'''



lst = [x for x in range(2,21,2)]
print(lst)

# Using list comprehension
lst2 = [x for x in range(1,21) if x%2==0]
print(lst2)


# Product of two list using normal way
a=[1,2,3,4,5]
b=[6,7,8,9,10]
z=[]

for i in range(len(a)):
    z.append(a[i]*b[i])

print(z)

# Product Using list comprehension

z= [a[x]*b[x] for x in range(len(a))]
print(z)

# common element in two list

c = [2,4,7,8,9]
d = [2,4,11,12,14]

lst3 = [c[x] for x in range(len(a)) if c[x]==d[x]]
print(lst3)
result = []

result = [i for i in c if i in d]
print(result)
