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