
# Find the sum 3 digit numbers 
# 345 -> 3+4+5 = 12 

num = int(input("Enter a 3 digit number: "))

a = num % 10

num = num // 10
b = num % 10

num = num // 10
c = num % 10

d = a+b+c 
print(d)