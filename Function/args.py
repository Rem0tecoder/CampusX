def multiply(*args):
    product = 1

    for i in args:
        product = product * i

    return product
    
x = multiply(2, 3, 4, 6, 8, 10)
print(x)
 