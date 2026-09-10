lower = int(input("Enter a lower range: "))
upper = int(input("Enter a upper range: "))

for i in range (lower, upper+1):
    for j in range (2, i):
        if i%j == 0:
            break
    else:
        print(i)