def f():
    def g():
        print('Inside function g')
    
    g()
    print('Inside function f')

f()


def g(x):
    def h():
        x = 'abc'
    x = x+1
    print('in g(x): x =', x)
    h()
    return x

x = 3 
z = g(x)


def g(x):
    def h(x):
        x = x+1
        print('in h(x): x = ', x)
    x = x + 1
    print('in g(x) x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z =', z)