
# FUNCTION CALLING

def greet(name) -> str:
    print(f"Hello {name}!! Nice to meet you")

greet("ABC")
greet("DEF")
greet("GHI")
#-------------------------------------------------------------------------------------
def add(a,b=5):
    print(a+b)
add(b=8)
add(b=5)
add(a=10,b=5)
add(a=20)

#-------------------------------------------------------------------------------------

def sd(*args, **kwargs):
    print("positional args : ", args)
    print("key positional args : ", kwargs)


sd(10,20,30,name = "abc", age = 23, city = "Munich")

#-------------------------------------------------------------------------------------

def call(a,b='Turin, Italy.'):
    print(f"the {a} is in {b}")

call("stadium")

#-------------------------------------------------------------------------------------
# 1 1 2 3 5 8 13
#fibonacci
x = fib(6)
print(x)

