# Case 1 - if the file is not present
f = open('sample.txt', 'w')
f.write('Hello World')
f.close()

# Write multiple line strings
f = open('saample1.txt', 'w')
f.write('Hello world')
f.write('\nhow are u')
f.close()

# case 2 write in already present file
f = open('sample.txt', 'w')
f.write('Hello brother')
f.close()

# introducing append mode
f = open('saample1.txt', 'a')
f.write('\nI am Fine')
f.close() 