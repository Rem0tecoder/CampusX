class User: # Parent class

    def __init__(self):
        self.name = 'nitish'

    def login(self):
        print('login')

class Student(User): # Child class

    #def __init__(self):
     #   self.rollno = 100

    def enroll(self):
        print('enroll into the course')

u = User()
s = Student()

print(s.name)
s.login()
s.enroll()

# Constructor Example

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


# Constuctor example 2

class Phone:

    def __init__(self, price, brand, camera):
        print('Inside the phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print('Inside SmartPhone constructor')

s = SmartPhone("Android", 2)


# Child can't access private members of the class
class Phone:

    def __init__(self, price, brand, camera):
        print('Inside the phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

    def show(self):
        print(self.__price)

class SmartPhone(Phone):
    def check(self):
        print(self.__price)

s = SmartPhone(20000, "Apple", 13)


