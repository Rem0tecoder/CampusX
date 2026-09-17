# Object without a reference
class Person:
    def __init__(self):
        self.name = 'Saurabh'
        self.gender = 'male'

p = Person()
q = p
print(q)
print(p)

# Multiple Ref
print(id(p))
print(id(q))


# Change the attributes value with the help of 2nd object
print(p.name)
print(q.name)
q.name = 'yadav'
print(q.name)
print(p.name)