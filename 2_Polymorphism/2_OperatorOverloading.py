# Operator Overloading --> +,*,- etc


"""
Adding additional functionality to the Operator.
 __add__ --> called whenever we use + operator (a+b).
 __gt__ --> called > operator (a>b)
Like this to perform every action we have special methods in behind.

"""

# # Example1: Adding Complex number is not possible ,lets make it with polymorphism
# class ComplexNumber:
#     def __init__(self,r,i):
#         self.real = r
#         self.imaginary = i
#         print(f"{self.real} & {self.imaginary}")

#     def __add__(self,other):
#         real = self.real + other.real
#         img = self.imaginary + other.imaginary
#         return f"{real}+{img}j"

# c1 = ComplexNumber(3,6)
# c2 = ComplexNumber(4,5)
# print(c1+c2)


## Example 2 : 
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __gt__(self,other):
        print('Elder Age check')
        if self.age > other.age:
            return f"{self.name} pay the bill"
        else:
            return  f"{other.name} pay the bill"
        

p1 = Person('Ram',23)
p2 = Person('sam',25) 
print(p1>p2)



