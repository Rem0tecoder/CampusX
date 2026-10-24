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