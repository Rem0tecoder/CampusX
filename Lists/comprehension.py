# Add 1 to 10 numbers to a list

L = []

for i in range (1, 11):
    L.append(i)

print(L)

# List Comprehension Method
L = [i for i in range(1, 11)]
print(L)

# Scalar multiplication on a vector.

v = [2, 3, 4]
s = -3

x = []
for i in v:
    x.append(i * s)

print(x)

# List Comprehension Method
res = [s*i for i in v]
print(res)

# Add Squares
L = [1, 2, 3, 4, 5]
x = []

for i in range(1, 6):
    x.append(i ** 2)

print(x)

# List Comprehension Method
res = [i ** 2 for i in L]
print(res)

# Print all numbers divisible by 5 in the range of 1 to 50.
x = []
for i in range(1, 51):
    if i%5 == 0:
        x.append(i)

print(x)

# List Comprehension Method
res = [i for i in range(1, 51) if i%5 ==0]
print(res)

# Find languages which start with letter p.
lang = ['java', 'python', 'php', 'c', 'javascript']
x = []
for i in lang:
    if i.startswith('p'):
        x.append(i)
        print(x)

# List Comprehension Method
res = [lang for lang in lang if lang.startswith('p')]
print(res)

# Nested if with List Comprehension.
basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'.

res = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
print(res)

# Print a (3,3) matrix using list comprehension -> Nested List Comprehension.
res = [[i*j for i in range(1,4)] for j in range(1,4)]
print(res)

# Cartesian product -> List comprehension on 2 lists together
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
res = [i*j for i in L1 for j in L2]
print(res)



# Itemwise
L = [1, 2, 3, 4]
for i in L:
    print(i)


# Indexwise
L = [1, 2, 3, 4]
for i in range(0, len(L)):
    print(L[i])


# Zip
L1 = [1, 2, 3, 4]
L2 = [-1, -2, -3, -4]
list(zip(L1, L2))
res = [i+j for i,j in zip(L1, L2)]
print(res)