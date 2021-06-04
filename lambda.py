'''def cube(n):
    return n**3
print(cube(2))'''

f = lambda x: x ** 3
print(f(3))


print("Even or odd using lambda function")
l =lambda x: 'YES'if x%2==0 else 'NO'
print(l(10))
print(l(15))

print("Sum of two number using lambda")
l2 = lambda a,b:a+b
print(l2(10,20))