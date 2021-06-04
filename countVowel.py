word = input("Enter the word")
vowel = {'a', 'i', 'e', 'o', 'u'}
dict = {}

for c in word:
    if c in vowel:
        dict[c] = dict.get(c, 0) + 1


for k, v in dict.items():
    print(k, "is present ", v, "times")

for k, v in sorted(dict.items()):
    print(k, "is present ", v, "times")
