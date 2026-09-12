# del

L = [1, 2, 3, 4, 5]
del L[-1]
del L[3: 4]
print(L)

# Remove
L = [1, 2, 3, 4, 5]
L.remove(5)
print(L)

# Pop
L = [1, 2, 3, 4, 5]

L.pop(2)
L.pop()
print(L)

# Clear
L = [1, 2, 3, 4, 5]
L.clear()
print(L)