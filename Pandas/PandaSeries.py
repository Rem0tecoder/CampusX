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

#
