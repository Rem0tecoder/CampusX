# print 1 to 10 numbers and their squares
a = {i:i**2 for i in range(1, 11)}
print(a)

# using existing dict
dist = {'delhi': 1000, 'mumbai': 2000, 'banglore': 3000}
print(dist.items())
miles = {key:value*1.6 for (key,value) in dist.items()}
print(miles)

# using zip
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_c = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]
f = {i:j for (i,j) in zip(days,temp_c)}
print(f)

# using if condition
products = {'phones': 10, 'laptop': 0, 'charger': 40, 'tablet': 0}
w = {key:value for (key,value) in products.items() if value>0}
print(w)

# Nested Comprehension
# print tables of numbers from 2 to 4
t = {i:{j:i*j for j in range(1, 11)} for i in range(2, 5)}
print(t)