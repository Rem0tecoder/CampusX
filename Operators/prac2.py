# min of 3 numbers

a = int(input("Enter a number : "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a < b and a < c:
    print("Smallest Number is: ", a)

elif b <c:
    print("Smallest Number is:", b)
else:
    print("Smallest Number is:", c)
