class Parent:

    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):

    def show(self):
        print("this is child class")

son = Child(100)
print(son.get_num())
son.show()

# example 4

class Parent:

    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):

    def __init__(self, val, num):
        self.__val = val

    def get_val(self):
        return self.__val

son = Child(100,10)
# print("Parent: Num", son.get_num())
print("Child: Val:", son.get_val())


# Example 5

class A:

    def __init__(self):
        self.var1 = 100

    def display1(self, var1):
        print("class A:", self.var1)

class B(A):

    def display2(self, var1):
        print("class B :", self.var1)

obj = B()
obj.display1(200)

# Method Overriding

class Phone:

    def __init__(self, price, brand, camera):
        print("Inside the phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")

s = SmartPhone(20000, 'apple', 13)
s.buy()


# Super Keyword

class Phone:

    def __init__(self, price, brand, camera):
        print("Inside the phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        # syntax to call parent's buy method
        super().buy()

s = SmartPhone(20000, 'apple', 13)
s.buy()

# Super Constructor

class Phone:

    def __init__(self, price, brand, camera):
        print("Inside the phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        print("inside the smartphone constructor")
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("inside the smartphone constructor")

s = SmartPhone(200000, 'samsung', 12, 'android', 2)
print(s.os)
print(s.brand)