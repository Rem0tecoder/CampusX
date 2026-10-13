# Normal Indexing and slicing

import numpy as np

a = np.arange(24).reshape(6,4)
print(a)
print(a[1,2])

# Fancy Indexing
print(a[[0,2,3]])
print(a[[0,2,3,5]])
print(a[:,[0,2,3]])

# Boolean Indexing

a = np.random.randint(1,100,24).reshape(6,4)
print(a)

# Find all numbers greater than 50
print(a[a>50])

# Find out even numbers

print(a%2 == 0)
print(a[a%2 ==0])

# find all numbers graeter than 50 and are even
print((a>50) &  (a%2 ==0))
print(a[(a>50) &  (a%2 ==0)])