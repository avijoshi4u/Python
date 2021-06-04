x = 123


def display():
    x = 658
    print(x)
    print(globals()['x'])


print(x)
display()

# Assign a function to a variable
print("Assign a function to a variable")
z = display
z()
z()

print("Function inside function")


def display1(name):
    def message():
        return "Hello "

    result = message() + name
    return result


print(display1("Sapna"))

print("Function as a parameter")


def display3(fun):
    return "Hello " + fun


def name(str):
    return str


print(display3(name("Aarna")))


# Return function
def disp():
    def message():
        return "hello"

    return message


funt = disp();
print(funt())

# pass list as parameter to function
def displayList(lst):
    for i in lst:
        print(i)

displayList([1,2,3,4])
