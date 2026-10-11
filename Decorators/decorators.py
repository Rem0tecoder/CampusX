# Python are 1st class Function
def func():
    print('Hello')

a = func
a()

# Example
def my_decorator(func):
    def wrapper():
        print('************')
        func()
        print('***********')
    return wrapper

def hello():
    print('Hello')

def display():
    print('Hello Saurabh')

a = my_decorator(hello)
a()
b = my_decorator(display)
b()