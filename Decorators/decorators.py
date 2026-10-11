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

# Better Syntax
def my_decorator(func):
    def wrapper():
        print('************')
        func()
        print('***********')
    return wrapper

def hello():
    print('Hello')


@my_decorator
def display():
    print('Hello Saurabh')

hello()

# Anything meaningful
# Execution time of function

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        print('time taken by', func.__name__,time.time()-start,'secs')
    return wrapper

@timer
def xyz():
    print('HEllo world')
    time.sleep(2)

@timer
def display():
    print('Displaying something')
    time.sleep(4)

xyz()
display()