rows = int(input("Enter the size of the row: "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        if j==1 or i == rows or i ==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() 