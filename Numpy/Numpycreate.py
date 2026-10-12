import numpy as np

a = np.array([1,2,3])
print(a)

# 2D and 3D

b = np.array([[1,2,3],[4,5,6]])
print(b)

c = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(c)

# dtype
x = np.array([1,2,3], dtype=float)
print(x)

# np.arange
y = np.arange(1,11)
print(y)

# with reshape
y = np.arange(1,11).reshape(5,2)
print(y)

# np.ones and np.zeros
z = np.ones((3,4))
print(z)

xx = np.zeros((3,4))
print(xx)

# np.random
yy = np.random.random((3,4))
print(yy)

# np.lispace
s = np.linspace(-10,10,10)
print(s)

# np.identity 
t = np.identity(3)
print(t)