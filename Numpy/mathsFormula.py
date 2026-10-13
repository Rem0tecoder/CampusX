# sigmoid
import numpy as np

def sigmoid(array):
    return 1/(1+np.exp(-(array)))

a = np.arange(10)
print(sigmoid(a))

# mean sqared error

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

print(actual)
print(predicted)

def mse(actual,predicted):
    return np.mean((actual-predicted)**2)

print(mse(actual,predicted))