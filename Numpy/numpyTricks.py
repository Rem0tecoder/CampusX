
import numpy as np
a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)
print(a)
print(b)
# sort
print(np.sort(a))
print(np.sort(b, axis=0))


# Append
print(np.append(a,200))
# print(np.append(b,np.ones(b.shape[0],1)),axis=1)

# Concatenate
c = np.arange(6).reshape(2,3)
d = np.arange(6,12).reshape(2,3)
print(np.concatenate((c,d),axis=0))

# np.unique
e = np.array([1,1,2,2,3,3,4,4,5,5,6,6])
print(np.unique(e))

# np.expand_dims 
print(np.expand_dims(a,axis=1))

# np.where

print(np.where(a>50))
# replace all values > 50
print(np.where(a>50,0,a))

# np.argmax
print(np.argmax(b, axis=0))

# np.argmin
print(np.argmin(a))

# np.cumsum
print(np.cumsum(a))
print(np.cumsum(b, axis=0))

# np.cumprod
print(np.cumprod(a))

# np.percentile
print(np.percentile(a,100))

# np.histogram
print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100]))

# np.corrcoef
salary = np.array([10000,20000,35000,40000,50000])
experience = np.array([1,2,3,4,5])
print(np.corrcoef(salary,experience))

# np.isin
items = [10,20,30,40,50,60,70,80,80,100]
print(a[np.isin(a,items)])

# np.put
print(np.put(a,[0,1],[110,300]))
print(a)

# Set Functions
# np.union1d
m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])
print(np.union1d(m,n))
print(np.intersect1d(m,n))
print(np.setdiff1d(m,n))
print(np.setxor1d(m,n))
print(np.in1d(m,n))

# np.clip
print(np.clip(a,a_min=25,a_max=75))