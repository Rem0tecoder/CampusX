# x -> x^2
res = lambda x: x**2
print(res(4))

# x,y -> x+y
re = lambda x,y : x+y
print(re(3,4))

# Check if a string has 'a'
a = lambda s:'a' in s
print(a('hello'))

# odd or even
a = lambda x:'even' if x%2 ==0 else 'odd'
print(a(6))

# Higher order functions
def square(x):
    return x**2

def transform(f, L):
    output = []
    for i in L:
        output.append(f(i))

    print(output)

L = [1,2,3,4,5]

transform(lambda x: x**3,L)




#   MAP
# square the items of alist
res = list(map(lambda x:x**2, [1,2,3,4,5]))
print(res)


# odd/even labelling of list items
L = [1,2,3,4,5]
x = list(map(lambda x: 'even' if x%2 ==0 else 'odd', L))
print(x)

# numbers greater than 5
L = [3,4,5,6,7]
res = list(filter(lambda x: x>5, L))
print(res)

# fetch fruits starting with 'a'
fruits = ['apple', 'guava', 'orange']
y = list(filter(lambda x: x.startswith('a'), fruits))
print(y)

# Reduce
# Sum of all item

import functools

x = functools.reduce(lambda x,y:x+y,[1,2,3,4,5]) 
print(x)

# find min
x = functools.reduce(lambda x,y:x if x<y else y, [23,11,10,5])
print(x)