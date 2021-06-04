def average(a, b):
    return (a + b / 2)


print(average(10, 20))


def cal(a, b):
    x = a + b
    y = a - b
    z = a * b
    u = a / b
    return x, y, z, u


result = cal(20, 10)
print(cal(20, 10))
for i in result:
    print(i)

# passing arguments as a keyword
print("passing arguments as a keyword")


def average2(x, y):
    print(x)
    print(y)
    return ((x + y) / 2)


print(average2(y=10, x=20))

# passing default arguments as a keyword
print("Default arguments as a keyword")
def average3(a=30, b=10):
    print(a)
    print(b)
    return ((a + b) / 2)


print(average3())
