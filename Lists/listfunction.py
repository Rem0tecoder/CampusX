# len

L = [2, 3, 4, 5, 6]
print(len(L))

# min

print(min(L))

# max
print(max(L))

# sorted
print(sorted(L, reverse=True))

# count
L = [1,4, 5, 6, 9, 5, 9,22]
print(L.count(0))

# Index 
L = [1,4, 5, 6, 9, 5, 9,22]
print(L.index(4))

# reverse
L = [1,4, 5, 6, 9, 5, 9,22]

L.reverse()
print(L)

# sort
L = [1,44, 56, 6, 9, 5, 79,22]
print(L)
print(sorted(L))
print(L)
L.sort()
print(L)

# Copy
L = [1,4, 5, 6, 9, 5, 9,22]
print(L)
print(id(L))
L1 = L.copy()
print(L1)
print(id(L1))

