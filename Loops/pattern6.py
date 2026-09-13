rows = int(input("Enter the size of the row: "))

for i in range(1, rows+1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print("*", end=" ")

    print()

for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print("*", end=" ")
    print()