import random
import mod as m
from collections import defaultdict

l = defaultdict(int)

for i in range(101):
    x = random.randint(1, 11)
    l[x] += 1

val_list = list(l.values())  
a = sorted(val_list)
b = sorted(val_list, reverse=True)

print(a)
print(b)


x = m.checkEven(1, 40)
print(x)

x = m.checkPrime(1,55)
print(x)

x = m.factorial(4)
print(x)