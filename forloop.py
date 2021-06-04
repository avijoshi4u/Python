for x in range(50, 71, 3):
    print(x)

lst = [1, 2, 3, 4, 5]
prod = 1
for z in lst:
    prod *= z
print("Product is", prod)

lst2 = [3, 5, 6, 9, 5, 12]
for k in lst2:
    if k == 5:
        break
    else:
        print(k)

print("continue example")
for j in range(3, 21):
    if j % 3 == 0 and j%2:
        continue
    else:
        print(j)
