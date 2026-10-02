# let's create a file
with open('saample.txt', 'w') as f:
    f.write('Hello world')

# try catch demo
try:
    with open('saample3.txt', 'r') as f:
        print(f.read())
except:
    print('Sorry file not found')


# catching specific exception
try:
    f =open('saample.txt', 'r')
    print(f.read())
    print(m)
    L = [1,2,3]
    print(L[100])
except FileNotFoundError:
    print('file not found')
except NameError:
    print('Variable not found')

# generic exception
except Exception as e:
    print(e)