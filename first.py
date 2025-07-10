

#CONDITIIONALS


count = 1
while count <= 10:
    print(count)
    count += 1
for LETTER in "HELLO":
    print(LETTER)

#---------------------------------------------------------------------------------


class Demo:
    def __init__(self, x):
        self.__x = x

    def show(self):
        print(self.__x)

d = Demo(10)
d.show()
# print(d._Demo__x)
# x = bool([])
# print(x)


# class A:
class Counter:
    def __init__(self, limit):
        self.limit = limit

    def count_up(self):
        for i in range(1, self.limit + 1):
            print(i, end=' ')

c = Counter(3)
c.count_up()
  
i = 0
while i < 3:
    i += 1
    if i == 2:
        continue
    print(i)

class Hostel:
    def __init__(self, type, prices):
        self.type = type
        self.prices = prices
    def fix (self):
        print(self.type)
        print(self.prices)

b1 = Hostel("boys", 20000)
# print(b1.type)
# print(b1.prices)
def calc(x):
    return x + 10

print(calc(5), calc('5'))
class A:
    def speakA(self):
        print("A speaks")

class B(A):
    def speakB(self):
        print("B speaks")

obj = B()
obj.speakA()
obj.speakB()

class rectangle:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth
    def area(self):
        return self.l * self.b

r = rectangle(4,4)
print(r.area())











