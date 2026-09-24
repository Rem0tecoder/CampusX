# with
with open('saample1.txt', 'w') as f:
    f.write('Tom and Jerry')

# try f.read() to read file using with
with open('sample.txt', 'r') as f:
    print(f.read())


# moving eithin a file -> 10 char then 10 char
with open('sample.txt', 'r') as f:
    print(f.read(10))
    print(f.read(10))


# benifit -> to load a big file in memory
big_L = ['hello world\n' for i in range(1000)]

with open('big.txt', 'w') as f:
    f.writelines(big_L)


with open('big.txt', 'r') as f:
    chunk_size = 100

    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size), end='***')
        f.read(chunk_size)


# seek and tell function
with open('sample.txt', 'r') as f:
    print(f.read(10))
    print(f.tell())
    f.seek(0)
    print(f.read(10))
    print(f.tell())


# Seek during write
with open('sample.txt', 'w') as f:
    f.write('hello')
    f.seek(0)
    f.write('x')