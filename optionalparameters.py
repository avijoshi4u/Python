"""
Here *args is optional parameter it is not mandatory to provide them
**Kwargs is optional key word parameter it is not mandatory to provide them
"""


def myfun(x, *args, **Kwargs):
    print(x)
    Kwargs['id'] ="1000"
    for each_args in args:
        print(each_args)
    for key, value in Kwargs.items():
        print(key , value)

    modified_args =args+(50,)
    fun(*modified_args, **Kwargs)
    return x

def fun(*args, **Kwargs):
    print(args)
    print(Kwargs)


print(myfun(10, 20, 30, 40, name="Sapna", age="30", salary=2000000))
