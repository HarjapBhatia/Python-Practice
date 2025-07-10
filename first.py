# b = 'Ronaldo'
# c = '40'
# print(f'His name is {b}. He is {c} years old.')
# print('His name is {}. He is {} years old.'.format(b,c))

# s = "pyPYeijfsf"
# print('py' in s)
# print('PY' in s)
# print('pY' in s)
# print('Ye' in s)

# email = input("enter: ")
# if '@' in email and email.endswith('.com'):
#     print("valid")
# else:
#     print("invalid")

# If the age is equal of greater than 18 he is eligible for voting , 
# if the age is equal to 40 is known a s actual voter,
#  if the age is more than 75 then he is a retired voter , 
# if age is less than 18 not eligible for voting
# age = int(input("enter the age : "))
# # if age == 40: print("actual voter")
# # elif age > 75: print("retired voter")
# # elif age >= 18: print("eligible for voting")
# # else: print("not eligible for voting")
# if 18<=age<40: print("eligible for voting")
# elif age == 40: print("actual voter")
# elif 41 <= age <75 : print("eligible for voting (senior)")
# elif age >= 75: print("retired voter")
# else: print("not eligible for voting")

# count = 1
# while count <= 10:
#     print(count)
#     count += 1
# for LETTER in "HELLO":
#     print(LETTER)

#---------------------------------------------------------------------------------
# problem-1
# num = int(input())
# if num > 0: print("positive")
# elif num < 0: print("negative")
# else: print("zero")


# # problem-2
#     if (i%3 != 0):
#         print(i)


# # problem-3
# while(True):
#     x = int(input())
#     if x>=0:
#         print("ok")
#     else:
#         print("loop end!!!")
#         break
#------------------------------------------------------------------------------------

# def greet(name) -> str:
#     print(f"Hello {name}!! Nice to meet you")

# greet("ABC")
# greet("DEF")
# greet("GHI")

# def add(a,b=5):
#     print(a+b)
# add(b=8)
# add(b=5)
# add(a=10,b=5)
# add(a=20)

# def sd(*args, **kwargs):
#     print("positional args : ", args)
#     print("key positional args : ", kwargs)


# sd(10,20,30,name = "abc", age = 23, city = "Munich")

# def call(a,b='Turin, Italy.'):
#     print(f"the {a} is in {b}")

# call("stadium")

# 1 1 2 3 5 8 13

# x = fib(6)
# print(x)


# x = 24

# def call():
#     global x
#     x = 1
#     return x
# call()

# print(x)
# print(call())
# print(x)

# import random
# from collections import defaultdict

# l = defaultdict(int)

# for i in range(101):
#     x = random.randint(1, 11)
#     l[x] += 1

# val_list = list(l.values())  
# a = sorted(val_list)
# b = sorted(val_list, reverse=True)

# print(a)
# print(b)

# from mod import checkEven

# x = checkEven(1, 40)
# print(x)

# from mod import checkPrime
# x = checkPrime(1,55)
# print(x)

# from mod import factorial
# x = factorial(4)
# print(x)


# class Demo:
#     def __init__(self, x):
#         self.__x = x

#     def show(self):
#         print(self.__x)

# d = Demo(10)
# d.show()
# # print(d._Demo__x)
# # x = bool([])
# # print(x)


# # class A:
# class Counter:
#     def __init__(self, limit):
#         self.limit = limit

#     def count_up(self):
#         for i in range(1, self.limit + 1):
#             print(i, end=' ')

# c = Counter(3)
# c.count_up()
  
# i = 0
# while i < 3:
#     i += 1
#     if i == 2:
#         continue
#     print(i)

# class Hostel:
#     def __init__(self, type, prices):
#         self.type = type
#         self.prices = prices
#     def fix (self):
#         print(self.type)
#         print(self.prices)

# b1 = Hostel("boys", 20000)
# # print(b1.type)
# # print(b1.prices)
# def calc(x):
#     return x + 10

# print(calc(5), calc('5'))
# class A:
#     def speakA(self):
#         print("A speaks")

# class B(A):
#     def speakB(self):
#         print("B speaks")

# obj = B()
# obj.speakA()
# obj.speakB()

# from mod import checkPrime
# x = checkPrime(2,100)
# print(x)



# import math
# r = int(input("enter radius : "))
# area = math.pi * r *r
# print(area)

# import calc as c

# w = c.add(3,4)
# x = c.sub(3,4)
# y = c.mult(3,4)
# z1 = c.div(3,4)
# z2 = c.div(3,0)

# print(w)
# print(x)
# print(y)
# print(z1)
# print(z2)


class rectangle:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth
    def area(self):
        return self.l * self.b

r = rectangle(4,4)
print(r.area())











