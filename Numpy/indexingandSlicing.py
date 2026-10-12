# Indexing and Slicing

import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

print(a1)
print(a2)
print(a3)

print(a2[2,3]) # 2-> row and 3 -> column
print(a3[1,0,1])
print(a3[0,0,0])
print(a3[1,1,0])

# 2D slicing
print(a2[:1])
print(a2[0,:])
print(a2[:,2])
print(a2[1:,1:3])
print(a2[::2,::3])
print(a2[::2,1::2])
print(a2[1,::3])
print(a2[0:2,1::2])

a4 = np.arange(27).reshape(3,3,3)
print(a4[0,1,:])
print(a4[1,:,1])
print(a4[2,1:,1:])
print(a4[::2,0,::2])

# Iterating

for i in a1:
    print(i)

# 2D

for i in a2:
    print(a2)

# 3D

for i in a3:
    print(i)


for i in np.nditer(a3):
    print(i)


# Transpose
print(np.transpose(a2))
print(a2.T)

# Ravel
print(a2.ravel())