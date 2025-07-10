# problem-1 : check the number positive, negative or zero!! 
num = int(input())
if num > 0: print("positive")
elif num < 0: print("negative")
else: print("zero")


# problem-2 : loop until the input number is negative!!
while(True):
    x = int(input())
    if x>=0:
        print("ok")
    else:
        print("loop end!!!")
        break


# problem - 3 :
# If the age is equal of greater than 18 he is eligible for voting , 
# if the age is equal to 40 is known a s actual voter,
#  if the age is more than 75 then he is a retired voter , 
# if age is less than 18 not eligible for voting

#method 1:
# age = int(input("enter the age : "))
# if age == 40: print("actual voter")
# elif age > 75: print("retired voter")
# elif age >= 18: print("eligible for voting")
# else: print("not eligible for voting")

#method 2:
if 18<=age<40: print("eligible for voting")
elif age == 40: print("actual voter")
elif 41 <= age <75 : print("eligible for voting (senior)")
elif age >= 75: print("retired voter")
else: print("not eligible for voting")