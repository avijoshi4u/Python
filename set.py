s = {10,20,30,"XYZ",20}
# set doesn't allow duplicates it simply omit the duplicate
print(s)

# to update the set
s.update([88,99])
print(s)

# set doesn't preserve insertion order and hence slicing, repetition,indexing are supported

#print(s[2])
#print(s*2)
#print(s[0:3])

# remove the element from set
s.remove("XYZ")
print(s)

# frozen set can't be modified. You can't perform update and remove opertaion on frozen set

f = frozenset(s)
print(type(f))
#f.update([4,6])
#f.remove(4)