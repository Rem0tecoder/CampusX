import numpy as np
import pandas as pd

# Creating DataFrame 
# using lists

student_data = [
    [100,80,10,0,0],
    [90,70,7,0,0],
    [120,100,14,0,0],
    [80,50,4,0,0]
]

x = pd.DataFrame(student_data,columns=['iq','marks','package'])
print(x)

# using dict

student_dict = {
    'iq': [100,90,120,80],
    'marks': [80,70,100,50],
    'package': [10,7,14,4]
}
students = pd.DataFrame(student_dict)
print(students)

# using read_csv
movie = pd.read_csv(r"C:\Users\eryad\Downloads\movies.csv")
print(movie)

ipl = pd.read_csv(r"C:\Users\eryad\Downloads\ipl-matches.csv")
print(ipl) 

# Data Frame Attributes and methods
# shape
print(movie.shape)
print(ipl.shape)

# dtpyes
print(movie.dtypes)
print(ipl.dtypes)

# index
print(movie.index)
print(ipl.index)

# columns
print(movie.columns)
print(ipl.columns)

# values
print(movie.values)
print(ipl.values)

# head and tail
print(movie.head())
print(ipl.tail(2))

# Sample
print(movie.sample(5))
print(ipl.sample(5))

# info
print(movie.info())
print(ipl.info())

# describe
print(movie.describe())
print(ipl.describe())

# isnull
print(movie.isnull())
print(ipl.isnull().sum())

# Duplicated
print(movie.duplicated().sum())
print(ipl.duplicated())

# Rename 
