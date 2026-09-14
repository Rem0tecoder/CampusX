# Empty Dictionary
dict  = {}
print(dict)

# 1D Dictionary
dict = {'name': 'Saurabh', 'age': '23'}
print(dict)

# with mixed keys
dict = {(1,2,3,4):1, 'name': 'saurabh'}
print(dict)

# 2D Dictionary
s = {
    'name':'saurabh',
    'college':'anduat',
    'sem':4,
    'subjects':{
        'DBMS': 50,
        'CN': 60,
        'OS': 70,
        'Python': 80,
        'DSA': 85
    }
}
print(s)

# Deleting items
del s ['subjects']['CN']
print(s)

# Editing key value pair
s['sem'] = 5
print(s)
s ['subjects']['Python'] = 90
print(s)

# Using sequence and dict function

# d4 = dict([(1,1),(2,2),(3,3)])
# print(d4)

# duplicate keys are not allowed
dict = {'name': 'Rahul', 'name': 'Piyush'}
print(dict)

# mutable items as keys not allowed
# dict = {'name': 'nitish',  [1,2,3]:2}
# print(dict)

# Accesssing items
my_dict = {'name': 'Jack', 'age': 27}
d = my_dict['name']
s = my_dict.get('age')
print(d)
print(s)

# Adding key-value pairs
my_dict = {'name': 'Oggy', 'age': 23}
my_dict['gender'] = 'male'
print(my_dict)

# Remove key-value pair
# popitem
z = {'name': 'Oggy', 'age': 23, 'gender': 'male'}
z.popitem()
print(z)


# Dictionary Operations
# Membership
d = {'name': 'Oggy', 'age': 55}
s = 'oggy' in d
print(s)

# Iteration
for i in d:
    print(i, d[i])


# items/keys/values
k = d.items()
print(k)

k = d.keys()
print(k)

k = d.values()
print(k)

# update
d1 = {1:2,3:4,4:5}
d2 = {4:7,6:8}
d1.update(d2)
print(d1)