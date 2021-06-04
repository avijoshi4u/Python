
def half(fun):
    def inner(n):
        result = fun(n)
        result= result/2
        return result
    return inner

@half
def num(n):
    return n

print(num(10))
