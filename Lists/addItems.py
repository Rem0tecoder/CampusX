# Append using for add a single item
L = [1, 2, 3, 4, 5]
L.append(10)
print(L)

# Extend using for add a multiple item at once
L = [1, 2, 3, 4, 5]
L.extend([6, 7, 8])
print(L)

# Insert 
L = [1, 2, 3, 4, 5]
L.insert(1, 100)
print(L)

# Editing Items In List
L = [1, 2, 3, 4, 5]
L[2] = 20

# editing with slicing
L[1:4] = [200, 300, 400] 
print(L)