""" on byte array we  cannot assign value
no slicing, no repetition is allowed on byte and byte array
we can assign a value to byte array"""

lst = [20, 30, 40, 50]
print(type(lst))
b = bytes(lst)
print(type(b))
#b[2] = 100
print(b[2])

b2 = bytearray(lst)
b2[2] = 100
print(b2[2])
