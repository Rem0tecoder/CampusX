# Union (|)
s1 = {1, 2, 3, 4,5}
s2 = {4, 5, 6, 7, 8}
s = s1 | s2
print(s)

# Intersection (&)
s = s1 & s2
print(s)


# Difference (-)
s = s1 - s2
print(s)

# Symmetric Difference (^)
s = s1 ^ s2
print(s)

# Membership Test
s = 1 in s1
print(s)

s = 10 in s1
print(s)

# Iretion
for i in s1:
    print(i)

# Funtions in sets
# Union/Update
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s = s1.union(s2)
print(s)


# Update 
s1.update(s2)
print(s1)
print(s2)

# Intersection/ Intersection_update
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s = s1.intersection(s2)
print(s)

# Intersection_update
s1.intersection_update(s2)
print(s1)
print(s2)


# isdisjoint
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s = s1.isdisjoint(s2)
print(s)

# issubset
s = s1.issubset(s2)
print(s)

# issuperset
s = s1.issuperset(s2)
print(s)

# Copy
s1 = {1,2,3}
s2 = s1.copy()
print(s1)
print(s2)