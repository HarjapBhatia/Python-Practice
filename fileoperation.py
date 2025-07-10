# opening and reading the file content

x = open("new.txt","r")
y = x.read()
print(y)
x.close()

# reading by line
x = open("new.txt","r")
y1 = x.readline()
y2 = x.readline()
y3 = x.readline()
print(y1 + y3)
x.close()
