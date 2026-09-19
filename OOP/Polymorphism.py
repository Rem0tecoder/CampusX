# Method Overloading

class Shape:

    """def area(self, radius):
        return 3.14*radius*radius

    def area(self, l, b):
        return l*b """

    def area(self,a,b=0):
        if b == 0:
         return 3.14*a*a
        else:
           return a*b
    
    

a = Shape()
print(a.area(2))
print(a.area(4, 5))





