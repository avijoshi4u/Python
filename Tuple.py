"""Tuple
Cann't be modified and it's immutable
insertion order is preserved
Duplicates allowed
hetreogenous elements are allowed
t1=(1,2,3,4)
or
t1=1,2,3,4
if contains only one elements should be ended by , otherwise it will be treated as variable
t3=1,
"""


tpl = (10,40,40,60,"xyz")
print(type(tpl))
print(tpl)
#tpl[2] = 90
print(tpl*3)
print(tpl.count(40))
print(tpl.index(60))

# convert list into tuple
lst=[10,50,70]
tpl2=tuple(lst)
print(type(tpl2))
print(tpl2)