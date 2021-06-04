import re

# if search method doesn't match anything it returns None and we can't apply group
str = "Take 1 up 1-3-2019 one 23 o idea.one idea 45 at a o Time on onionFresh 12-11-2020"
result = re.search(r'o\w\w', str)
print(result.group())

# findall method return a list containing all the matching pattern in a given string
result = re.findall(r'o\w\w', str)
print(result)

# Match method search for the pattern at the starting of the text
result = re.match(r'T\w\w', str)
print(result.group())

result = re.split(r'\d+', str)
print(result)

result = re.sub(r'one','Two',str)
print(result)

print("+ means one or more ")
result = re.findall(r'o\w+', str)
print(result)

print("* means zero or more ")
result = re.findall(r'o\w*', str)
print(result)

print("? means zero or one ")
result = re.findall(r'o\w*', str)
print(result)

print("? means zero or one ")
result = re.findall(r'o\w?', str)
print(result)

print("{n} exactly n occurrence of regular expr")
result = re.findall(r'o\w{2}', str)
print(result)

print("{n,m}  min n occurrence of regular expr and m is maxm occurrence of regular expr")
result = re.findall(r'o\w{1,4}', str)
print(result)


print("extract dates")
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result)

result = re.search(r'^T\w*', str)
print(result.group())


