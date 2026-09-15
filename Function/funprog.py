# Let's create a function (with docstring)

def is_even(num):
    """
    This function returns if a given number is odd or even
    input - any valid integer
    output - odd/even
    """
    if type(num) == int:


        if num % 2 == 0:
            return 'even'
        else:
            return 'Odd'
    else:
        return 'Not valid '
    


# function
# function_name(input)
for i in range(1, 11):
    x = is_even(i)
    print(x)