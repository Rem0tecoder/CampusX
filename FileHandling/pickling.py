# Pickling

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print('Hi my name is',self.name,'and i am',self.age,'yeas old')


p = Person('saurabh',23)

# pickle dump
import pickle
with open('pesron.pkl','wb') as f:
    pickle.dump(p, f)


# Pickle load
import pickle
with open('person.pkl', 'rb') as f:
    p = pickle.load(f)

p.display_info()