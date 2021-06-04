
s = "you are welcome."
print(s)
print(len(s))

# multiline string
s1 = """you are the
creator of your destiny.
Do you know?"""

print(s1)
# repeation of string
print(s * 2)
# indexing
print(s[4])

# slicing
print(s[0:5])
print(s[0:])
print(s[:8])
# start counting the index from end
print(s[-3:-1])

# steps
print(s[0:10:3])
print(s[::-1])
# how to strip out spaces
s3 = "  Hello to python   "
print(s3)
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())

# more important functions
print(s3.find("pyt"))
print(s3.find("py", 0))
# below "py" string that need to be searched, 0 is starting index and len(s3) is end index where your search will end
print(s3.find("py", 0, len(s3)))
print(s3.find("pym"))

# count function --> to count the no of occurrence
print(s3.count("ll"))
print(s3.replace("python", "Java"))
print(s3.upper())
print(s3.lower())
print(s3.title())

# check palindrome
str = "aabaar"
rev = str[len(str)::-1]
print(rev)
if str == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
