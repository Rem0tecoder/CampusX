# Array Attributes

import numpy as np

a1 = np.arange(10)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

print(a1)
print(a2)
print(a3)

# ndim  Dimension of array
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

# shape
print(a1.shape)
print(a2.shape)
print(a3.shape)

# size
print(a2.size)

# itemsize
print(a3.itemsize)

# dtype
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

# Changing Datatype
# astype
print(a3.astype(np.int32))

