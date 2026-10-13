# same shape
import numpy as np

a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)
print(a)
print(b)

print(a+b)
print('\n')
# Diff shape

a = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)
print(a)
print(b)

print(a+b)

# Examples

a = np.arange(12).reshape(4,3)
b = np.arange(3)

print(a)
print(b)

print(a+b)

a = np.arange(3).reshape(3,1)
b = np.arange(3).reshape(1,3)
print(a)
print(b)

print(a+b)
print('\n')


a = np.arange(12).reshape(3,4)
b = np.arange(12).reshape(4,3)
print(a)
print(b)

print(a+b)