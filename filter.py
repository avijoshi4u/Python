lst = [2, 10, 20, 15, 25]

result = list(filter(lambda x: x % 2 == 0,lst))
print(result)
for i in result:
    print(i)