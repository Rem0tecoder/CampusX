# Find the length of given string wyhout using the len() function

str = input("Enter a whole string: ")
counter = 0

for i in str:
    counter += 1

print('Lenght of the string is', counter)

# Extract User from the given email
# Eg email is eryadav001@gmail.com
# Then the username should be like eryadav001


str = input("Enter email: ")
pos = str.index('@')
print(str[0:pos]) 

# Count the frequency of a particular character in a provided string.
# Eg 'Hello how are you' is the string, the frequency of the h in this string is 2.

str = input('Enter a string: ')
term = input('What would u like to search for: ')
counter = 0
for i in str:
    if i == term:
        counter += 1

print('Frequency', counter) 

# Write a program which can remove a particular character from a string.
str = input('Enter a string: ')
term = input('What would u like to remove from the string: ')

result = ''

for i in str:
    if i != term:
        result = result + i

print(result) 

# Write a program that can check whether a given string is palindrome or not.
# abba 
# malyalam
str = input('Enter a string: ')
flag = True
for i in range (0, len(str)//2):
    if str[i] != str[len(str) - i -1]:
        flag = False
        print('Not a Palindrome')
        break

if flag:
    print('Palindrome') 



# Write a program to count the number of words in a string without using split().
str = input('Enter A string: ')
L = []
temp = ''
for i in str:

    if i != ' ':
        temp = temp + i
    else:
      L.append(temp)
      temp = ''

L.append(temp)
print(L) 

# Write a program to convert a string into the titele case without using the title().
str = input('Enter a string: ')
L = []

for i in str.split():
    L.append(i[0].upper() + i[1:].lower())

print(" ".join(L)) 

# Write a program to convert the integer into string.

num = int(input("Enter a number: "))

digits = '0123456789'
result = ''

while num != 0:
    result = digits[num % 10] + result
    num = num //10

print(result)












