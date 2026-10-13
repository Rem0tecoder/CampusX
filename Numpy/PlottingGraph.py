# Plotting graph 
# x = y
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
y = x
print(x)
print(y)

#plt.plot(x,y)
#plt.show()

# y = x^2
x = np.linspace(-10,10,100)
y = x**2

#plt.plot(x,y)
#plt.show()

# y = sin(x)
x = np.linspace(-10,10,100)
y = np.sin(x)



# Sigmoid graph
x = np.linspace(-10,10,100)
y = 1/(1+ np.exp(-x))
# plt.plot(x,y)
# plt.show()

# Plotting a scatter plot
