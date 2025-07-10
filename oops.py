
# -----------------------------------------------------------------------------------------------------------------------------------------------

#OOPs in PYTHON !!

# -----------------------------------------------------------------------------------------------------------------------------------------------

# 1. ENCAPSULATION
# -> It contains access modifiers, which restricts the access of methods/attributes.
# -> They are mainly of three type : public access modifier, private access modifier and protected access modifier.

# class employee:
#     def __init__(self,name,salary,experience):
#         self.name = name         # public access modifier
#         self.__sal = salary      # private access modifier(_)
#         self._exp = experience   # protected access modifier(__)
#     def show(self):
#         print(f"Name : {self.name}")
#         print(f"Salary (in Rs.) : {self.__sal}")
#         print(f"Experience (in yrs) : {self._exp}")

# b = employee("Het", 150, 2)
# b.show()         # it will print all of them
# print(b.name)    # it will print (cuz it is public)
# print(b._exp)    # it will print (cuz its protected (direct access is allowed))
# print(b.__sal)   # it will throw an error (it is private access modifier, hence direct access isn't allowed!)

# ERROR DURING PRIVATE ACCESSING => AttributeError: 'employee' object has no attribute '__sal'

        
# -----------------------------------------------------------------------------------------------------------------------------------------------

# 2. INHERITANCE
# -> It allows one class(child) to inherit attributes and methods from another class(parent). 

# class animal: 
#     def speak(self):
#         print("Animal Speaks!!")
# class Dog(animal):
#     def bark(self):
#         print("Dog Barks!!")

# d = Dog()
# d.speak()     # inherited method
# d.bark()      # child's own method

# -----------------------------------------------------------------------------------------------------------------------------------------------

# 3. POLYMORPHISM
# -> It refers to the ability to use the same intereface (like method name) for diffferent underlying forms (datatypes or classes)
# ->  one particular methods used in nesting/multiple times. 

# class animal:
#     def speak(self):
#         print("Animal makes sound")

# class dog(animal):
#     def speak(self):          # method overriding (overriding the method of animal) - runtime polymorphism
#         print("Dog barks")

# class cat(animal):
#     def speak(self):          # method overriding (overriding the method of animal) - runtime polymorphism  
#         print("cat meows")

# a = animal()
# b = dog()
# c = cat()

# a.speak()
# b.speak()
# c.speak()


# -----------------------------------------------------------------------------------------------------------------------------------------------

# 4. ABSTRACTION
# -> Hiding complex parts and showing necessary details only

from abc import ABC, abstractmethod 
class animal(ABC):    # ABC = abstract base class, if you add this into the class with the @ , it will abstract the class and hide the class
    @abstractmethod   # it will hide the complex class
    def sound2(self):
        print("ffdsffdsdf")

class dog(animal):
    def sound(self):
        print("bark!!")

d = dog()
d.sound()
d.sound2()
