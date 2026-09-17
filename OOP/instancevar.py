# instance var 
class Person:

    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input

p1 = Person('Oggy', 'india')
p2 = Person('Bob', 'Japan')

x = p2.name
print(x)