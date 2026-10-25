import pandas as pd
import numpy as np

# String
country = ['India', 'America', 'China', 'Japan']
print(pd.Series(country))

# Integer 
runs = [65,99,67,90,9,100]
print(pd.Series(runs))

# Custom Index
marks = [67,56,89,100]
subjects = ['maths', 'english', 'science', 'hindi']
print(pd.Series(marks,index = subjects))

# Setting a name
marks = [67,56,89,100]
subjects = ['maths', 'english', 'science', 'hindi']
print(pd.Series(marks,index = subjects, name= 'Bob marks'))

# Series from dict
marks = {
    'english': 67,
    'hindi': 99,
    'science': 90,
    'python': 98
}

marks_series  =pd.Series(marks, name='Bob Marks')
print(marks_series)

# Series Attributs
# size
print(marks_series.size)

#dtype
print(marks_series.dtype)

# name
print(marks_series.name)

# is_unique
print(marks_series.is_unique)

# index
print(marks_series.index)

# Values
print(marks_series.values)


# Series using read_csv
# with one col
subs = pd.read_csv(r"C:\Users\eryad\Downloads\subs.csv").squeeze('columns')
print(subs)

# with 2 cols
runs = pd.read_csv(r"C:\Users\eryad\Downloads\kohli_ipl.csv",index_col= 'match_no').squeeze('columns')
print(runs)

# Bollywood movies
mv = pd.read_csv(r"C:\Users\eryad\Downloads\bollywood.csv", index_col= 'movie').squeeze('columns')
print(mv)

# Series Method

# Head and tail
print(subs.head())
print(runs.head(3))

print(runs.tail(10))

# Sample
print(mv.sample(10))

# value_count -> movies
print(mv.value_counts())

# sort_values - > inplace
print(runs.sort_values(ascending=False))
print(runs.sort_values(ascending=False).head(1).values[0])

# sort_index -> inplace -> movies
print(mv.sort_index())


# Series Math Methods
# count
print(mv.count())
print(runs.count())

# sum -> product
print(subs.sum())
print(runs.sum())

# mean median Mode std var
print(subs.mean())
print(runs.median())
print(mv.mode())
print(subs.std())
print(subs.var())

# min/max
print(subs.min())
print(subs.max())

# describe
print(runs.describe())


# series Indexing
# int indexing
'''x = pd.Series[12,23,34,45,56,67,78]
print(x[0])'''

print(mv[0])

# slicing
print(runs[5:16])

# fancy indexing
print(runs[[1,3,4,5]])


# Editing Series
# using indexing
marks_series[1] = 100
print(marks_series)

# what if an index does not exist
marks_series['sst'] = 90
print(marks_series)

# Series with Python Functionality
# len/type/dir/sorted/max/min
print(len(subs))
print(type(subs))
print(dir(subs))
print(sorted(subs))
print(min(subs))
print(max(subs))

# type conversion
print(dict(marks_series))

# membership operator
print('Zindagi Tere Naam ' in mv.values)

# looping
for i in mv.index:
    print(i)

# Arithmetic 
print(100 - marks_series)

# Booleaning Indexing
# find no of 50's and 100's scored by vk
print(runs[runs > 50].size)

# plotting graph on series
import matplotlib.pyplot as plt
subs.plot()
plt.show()

mv.value_counts().head(20).plot(kind= 'pie')
plt.show()