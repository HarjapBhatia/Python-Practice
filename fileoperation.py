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

# writing in the file
x = open("new2.txt", "w")
x.write("this is 1st line\n")
x.write("this is 2nd line")
x.close()
