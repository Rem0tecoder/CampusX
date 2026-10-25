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

x = pd.DataFrame(
    student_data,
    columns=['iq','marks','package', 'col14', 'col15'])
print(x)

# using dict

student_dict = {
    'name': ['banti','abhi','anmol','anshu'],
    'iq': [100,90,120,80],
    'marks': [80,70,100,50],
    'package': [10,7,14,4]
}
students = pd.DataFrame(student_dict)
students.set_index('name',inplace=True)
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
df = students.rename(columns={'marks':'Percent','package':'lpa'})
print(df)

# Selecting cols form DataFrame
# Single col
print(movie['title_x'])
print(ipl['Venue'])

# Multiple col
print(movie[['title_x','year_of_release']])
print(ipl[['Team1','Team2','WinningTeam']])

# Selecting Rows
# single row
print(movie.iloc[0])

# Multiple rows
print(movie.iloc[0:5])

# Fancy Indexing
print(movie.iloc[[0,4,5]])

# using loc func
print(students.loc['abhi'])
print(students.loc['banti':'abhi'])

# selecting both rows and columns
print(movie.iloc[0:3,0:3])
print(movie.loc[0:2,'title_x':'poster_path'])


# Data Filtering
# find all final winners
mask = ipl['MatchNumber'] =='Final'
new_df = ipl[mask]
print(new_df[['Season',"WinningTeam"]])

# how many super over finishes have occured
df = ipl['SuperOver'] == 'Y'
new_df = ipl[df].shape[0]
print(new_df)

# how many matches has csk won in Kolkata
df = ipl[(ipl['City'] == 'Kolkata') & 
         (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0]
print(df)

# toss winner is match winner in percentage
df = ipl[ipl['TossWinner'] == ipl['WinningTeam']
         ].shape[0]/ipl.shape[0]*100
print(df)

# movies with rating higher than 8 and votes > 10000
df = movie[(movie['imdb_rating']> 8) &
            (movie['imdb_votes'] > 10000)].shape[0]
print(df)