# Serializing abd deserializing with custom object

class Person:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender


# format to printed in
# -> Saurabh Yadav age-> 23 gender -> male

person = Person('Saurabh',' Yadav',23, 'male' )

# as a string
import json

def show_object(person):
    if isinstance(person,Person):
        return "{} {} age-> {} gender -> {}".format(person.fname, person.lname, person.age, person.gender)

with open('demo.json', 'w') as f:
    json.dump(person, f, default=show_object)


# as dict
import json

def show_object(person):
    if isinstance(person,Person):
        return {'name': person.fname + ' ' + person.lname, 'age': person.age, 'gender': person.gender}

with open('demo.json', 'w') as f:
    json.dump(person, f, default=show_object, indent=4)


# deseerializing

with open('demo.json', 'r') as f:
    print(json.load(f))