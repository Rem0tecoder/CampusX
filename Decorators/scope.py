# local and global

a = 2
# global var

def temp():
    b = 3
    # local var

    print(b)

temp()
print(a)

# local and global (with same name)

a = 2
# global var

def temp():
    a = 3
    # local var

    print(a)

temp()
print(a)

# local and global -> local does not have but golabal has

a = 2
# global var

def temp():
    
    # local var

    print(a)

temp()
print(a)

# local and global -> Editing global

a = 2
# global var

def temp():
    
    # local var
    global a
    a +=2
    print(a)

temp()
print(a)

# local and global -> global inside the local


# global var

def temp():
    
    # local var
    global a
    a = 2
    print(a)

temp()
print(a)

# Local and global -> function parameter is local
def temp(z):
    print(z)

a = 5
temp(5)
print(a)

# built-in scope
import builtins
print(dir(builtins))
print('hello')

# renaming builtins

L = [1,2,3]

'''def max():
    print('hello')

max(L)'''

# Enclosing Scope
def outer():
    def inner():
        print('Inner function')
    inner()
    print('outer function')

outer()
print('main program')

# non local keyword
def outer():
    a = 1
    def inner():
        nonlocal a
        a += 1
        print('Inner function', a)
    inner()
    print('outer function', a)

outer()
print('main program')