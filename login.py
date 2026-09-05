# login program and indentation
# email -> eryadav001@gmail.com
# Password -> 1234


email = input('Enter your email: ')
password = input('Enter ypur password: ')

if email == "eryadav001@gmail.com" and password == "1234":
    print("Welcome")
elif email == "eryadav001@gmail.com" and password != "1234":
    print("Password is Incorrect")
    password = input("Enter password again: ")
    if password == "1234":
        print("Welcome")
    else:
        print("Tu Rehne De bhai")
else:
    print("Try again")