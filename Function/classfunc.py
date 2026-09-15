# type and id
def sqaure(num):
    return num**2

x = type(sqaure)
y = id(sqaure)
print(x)
print(y)

# Reassign
x = sqaure(4)
y = id(x)
print(x)
print(y)

# Deleting function
del sqaure
print(x)

# Returning Function
def f():
    def x(a, b):
        return a+b
    return x

val = f()(3, 4)
print(val)

# function as argument
def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_b')
    return z()

print(func_b(func_a)) 