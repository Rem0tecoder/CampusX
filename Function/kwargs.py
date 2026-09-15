def display(**kwargs):

    for (key, value) in kwargs.items():
        print(key, '->', value)

display(India ='Delhi', USA ='Washington', Australia ='Canbara', Japan = 'Tokyo')


# Without return statement
L = [1, 2, 3]
print(L.append(4))
print(L)
