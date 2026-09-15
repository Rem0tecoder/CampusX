def g(y):
    print(x)
    print(x+1)

x = 5
g(x)
print(x)

def f(y):
    x = 1
    x += 1
    print(x)

x = 5
f(x)
print(x)

def h(y):
    # global x
    x += 1
x = 5
h(x)
print(x)

def s(x):
    x = x + 1
    print('in s(x): x =', x)
    return x

x = 3
z = s(x)
print(' in main program scope: z =', z)
print('in main program scope: x =', x)