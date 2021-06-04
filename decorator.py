'''Decorator takes a function and it will return a function but the
function that is returned by the decorator will perform additional
logic or additional processing on the function given as input '''


def decor(fun):
    def inner():
        result = fun()
        return result * 2

    return inner


def num():
    return 5


result_decor = decor(num)
print(result_decor())
print(decor(num)())

print("Using @Decorator")


def decorfun(fun2):
    def inner():
        result = fun2()
        return result * 2

    return inner


@decorfun
def num2():
    return 5


print(num2())

print("Using decorator string")


def decorfunc(func):
    def inner(n):
        result = func(n)
        result += "How are you?"
        return result

    return inner


@decorfunc
def hello(name):
    return "Hello " + name


print(hello("Sapna "))
