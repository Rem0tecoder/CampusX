# Empty 
t1 = ()
print(t1)

# Create a tuple with a single item
t2 = (3,)
print(t2)

# Homogenous tuple
t3 = (1, 2, 3, 4)
print(t3)

# Hetrogenous tuple
t4 = (1, 2.5, True)
print(t4)

# tuple within tuple
t5 = (1,2, (3,4))
print(t5)

# using type conversion
t6 = tuple('hello')
print(t6)

# Operations in Tuple
# + and *
t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)
tup = t1+t2
print(tup)

# Tuple Unpacking
a,b,c = (1,2,3)
print(a,b,c)

a,b,d = (1,2,3)
print(a,b)

a = 1
b = 2
a,b = b,a
print(a,b)

a,b, *others = (1,2,3,4,5)
print(a,b)
print(others)

# Zipping tuples
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c= tuple(zip(a, b))
print(c)