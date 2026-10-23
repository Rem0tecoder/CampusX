
import numpy as np
a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)
print(a)
print(b)
# sort
print(np.sort(a))
print(np.sort(b, axis=0))

