# Polymorphism Concept Ducktyping will be learned here.

### Example -1 --> We dont need to declare the x type as int or float
def square(x):
    return x*x

print(square(5) )   
print(square(5.5))




### Example 2 -->

class Duck:
    def swim(self):
        print("I am a duck and I can swim")
    
    def speaks(self):
        print("Quack Qauck")
    

class Dog:
    def swim(self):
        print("I am a dog and I can swim")

    def speaks(self):
        print("woo woo")
    

class Person:
    def speaks(self):
        print("blah blah blah")


def display(obj):
    obj.swim()
    obj.speaks()
    print("Thank you...")

### Object Creation for Classes
obj1 = Duck()
obj2 = Dog()
obj3 = Person()





