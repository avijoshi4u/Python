x = 1
while x <= 20:
    print(x)
    x += 1

# odd number between two given number

y = int(input("Enter the min number"))
z = int(input("Enter the maximum number"))

if y % 2 == 0:
    y += 1
i = y
while i <= z:
    print(i)
    i += 2
