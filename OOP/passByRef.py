class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# Outside the class -> function
def greet(person):
    print('Hi my name is', person.name,'I am a', person.gender)
    person.name = 'ankit'
    print(person.name)
    

p = Person('nitish', 'male')
print(id(p))
x = greet(p)
print(id(p))
print(p.name)
