# Array Operations
import numpy as np
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)
print(a1)
print(a2)


# scalar operation
# Arithmetic
print(a1*3)

# relational
print(a1 > 4)

# Vector Operation
# Arithmetic
print(a1*a2)

# max/min/sum/prod
# 0-> col, 1-> row

a1 = np.random.random((3,3))
a1 = np.round(a1*100)
print(a1)
print(np.max(a1))
print(np.max(a1,axis=1))
print(np.min(a1))
print(np.sum(a1))
print(np.prod(a1))


# mean/median/std/var
print(np.mean(a1))
print(np.median(a1))
print(np.std(a1))
print(np.var(a1))

# trigonometric function
print(np.cos(a1))

# dot product

a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)
print(np.dot(a2,a3))

# log and exponent
print(np.log(a1))
print(np.exp(a1))

# round/floor/ceil
c = np.random.random((2,3))*100
print(np.floor(c))
print(np.ceil(a1))
print(np.round(a1))