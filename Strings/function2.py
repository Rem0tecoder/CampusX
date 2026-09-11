
# Capitalize
s = 'hello world'
s.capitalize()
print(s.capitalize())

# Title

str = 'hello world'
str.title()
print(str.title()) 

# Upper
str = 'Hello world'
str.upper()
print(str.upper())

# Lower
str = 'HELLO WORLD'
str.lower()
print(str.lower())

# Swapcase
str = 'Hello world'
str.swapcase()
print(str.swapcase())

# Count
str = 'Hello world'
str.count('l')
print(str.count('l'))

# Find 
str = 'My name is Saurabh'
str.find('is')
print(str.find('is'))

# Endswith
str = 'My name is saurabh'
print(str.endswith('bh'))

# startswith
str ='My name is Saurabh'
print(str.startswith('my'))

# Format
name = 'Saurabh'
gender = 'Male'
print('Hi my name is{} and i am a {}'.format(name,gender)) 

# Split
print('Hi my name is faah'.split('a'))

# Join
print(" ".join(['Hi my n', 'me is f', '', 'h']))

# Replace 
print('Hi my name is faah'.replace('faah', 'piyush'))

# Strip
print('faaah          '.strip())