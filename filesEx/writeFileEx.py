f = open("myfile.txt", "w")
print("Enter the text (Type # when you are done)")
s = ''
while s != '#':
    s = input()
    f.write(s+"\n")

f.close()