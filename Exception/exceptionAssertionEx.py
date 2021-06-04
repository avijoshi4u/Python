try:
    num = int(input("Enter the number"))
    assert num % 2 == 0, "You have entered an odd number"
except AssertionError as obj:
    print(obj)
print("After assertion")
