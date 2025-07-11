# ZERODIVISION ERROR

try: # try running respective code!!
    x = 23/0
except:   # if theres an error then return this !
    print("error!!")

# -------------------------------------------------------------

# VALUE ERROR

age1 = None
age2 = None

try:
    age1 = int(input("Enter age1 : "))
except ValueError:
    err1 = "Error: Please enter a valid number for age1!"

try:
    age2 = int(input("Enter age2 : "))
except ValueError:
    err2 = "Error: Please enter a valid number for age2!"

#returning the values with errors
if age1 is not None:
    print("Age 1 :", age1)
else:
    print(err1)
if age2 is not None:
    print("Age 2 :", age2)
else:
    print(err2)

# -----------------------------------------------------------------


#FILENOTFOUND ERROR

try:
    f = open('something.txt','r')  # non-existent file
    content = f.read()
    f.close()
except:
    print("error : file not found!")

# -----------------------------------------------------------------

#INDEX ERROR

l = [1,2,3,4,5]
try:
    print(l[5])
except IndexError:
    print("it's an index error!!")

