# Single Inheritance
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass

s = SmartPhone(20000, 'Apple', 13)
print(s.brand)
print(s.camera)
s.buy()


# Multilevel inheritance

class Product():
    def review(self):
        print("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside the phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass

s = SmartPhone(20000, "Apple", 12)
s.buy()
s.review()

# Hierarchical 

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside the phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass

class Feature(Phone):
    pass

SmartPhone(10000, "Samsung", "200px").buy()
Feature(1000, "Lava", "1Px").buy()

# Multiple
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside the phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class Product:
    def review(self):
        print("Customer review")

class SmartPhone(Phone, Product):
    pass

s = SmartPhone(20000, "Apple", "23px")
s.buy()
s.review()

# Diamond Problem
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside the phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class Product:
    def buy(self):
        print("Product buy method")

# Method resolution order
class SmartPhone(Phone, Product): # First one is execute first here phone method execute first
    pass

s = SmartPhone(20000, "Apple", "23px")
s.buy()


# Practice Question
class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        return 30
    
    def m2(self):
        return 40

class C(B):
    def m2(self):
        return 20

obj1 = A()
obj2 = B()
obj3 = C()
print(obj1.m1() + obj3.m1() + obj3.m2())

# Practice question 2

class A:

    def m1(self):
        return 20

class B(A):

    def m1(self):
        val = super().m1()+30
        return val

class C(B):
    def m1(self):
        val = self.m1()+20
        return val

obj = C()
print(obj.m1())


