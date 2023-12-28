class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
     # adding two objects 
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
 
Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2

print(Ob3)

print(complex.__add__(Ob1 , Ob2)) 

print(Ob1.__add__(Ob2))