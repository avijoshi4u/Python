from functools import reduce

lst = [10, 20, 30, 40]
func = reduce(lambda a, b: a + b, lst)
print(func)
