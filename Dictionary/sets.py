# Creating Set
# Empty set
s = set()
print(s)

# 1D AND 2D
s1 = {1, 2, 3}
print(s1)

"""s2 = {1, 2, 3, {4, 5}}
print(s2) """

# Homo and Hetro
s3 = {1, 'Hello', 2.59, True}
print(s3)

# using type conversion
s4 = set([1, 2, 3, 4])
print(s4)

# Duplicate not allowed
s5 = {1, 1, 2, 2, 3, 3}
print(s5)

# Set can't have mutable items
# s6  = {1, 2, [3, 4]}
# print(s6)

# Accessing itmes
"""set = {1, 2, 3, 4}
s = set[1]
print(s)    not allowed """

# Editing is also not allowed in sets

# Adding items
s= {1, 2, 3, 4}
s.add(10)
print(s)

# update
s.update([5, 6, 7])
print(s)

# Deleting items
# del
s = {2, 3, 4, 5}
# del s
# print(s)

# Discard
s.discard(2)
print(s)

# Remove
s.remove(4)
print(s)

# pop // Delete anything randomly
s.pop()
print(s)

# clear // delete all the elements from the sets
s.clear()
print(s)