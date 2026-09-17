# How Object access attributes

class Person:
    def __init__(self, name_input, country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == 'India':
            print("Namaste", self.name)
        else:
            print("Hello", self.name)

# how to access attributes
p = Person('saurabh', 'India')
x = p.name
print(x)
p.greet()

p.gender = 'male'
y = p.gender
print(y)
