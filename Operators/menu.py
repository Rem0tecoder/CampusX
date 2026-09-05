# menu driven calculator

fnum = int(input("enter 1st number: "))
snum = int(input("enter 2nd number: "))

op = input("Enter the operation: ")

if op == '+':
    print(fnum + snum)
elif op == '-':
    print(fnum - snum)
elif op == '*':
    print(fnum * snum)
else:
    print(fnum / snum)