# Speed 
# List

a = [i for i in range(10000000)]
b = [i for i  in range(10000000,20000000)]

c = []
import time
start = time.time()

for i in range(len(a)):
    c.append(a[i]+b[i])

print(time.time()-start)

# numpy
import numpy as np

a = np.arange(10000000)
b = np.arange(10000000,20000000)

start = time.time()

c = a+b

print(time.time()-start)

# Memory

a1 = [i for i in range(10000000)]
import sys

print(sys.getsizeof(a1))

# numpy
a2 = np.arange(10000000)
print(sys.getsizeof(a2))