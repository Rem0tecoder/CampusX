# reading from files
# using -> read()

f = open('sample.txt', 'r')
s = f.read()
print(s)
f.close()

# reading upto n characters
f = open('sample.txt', 'r')
s = f.read(10)
print(s)
f.close()


# readline() -> to read line by line
f = open('sample.txt', 'r')
s = f.readline()
print(s)
s1 = f.readline()
print(s1)
f.close()

# reading entire using readline
f = open('sample.txt', 'r')

while True:
    data = f.readline()

    if data == '':
        break
    else:
        print(data, end='')
f.close()