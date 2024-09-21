## Protected
"""
In actual Protected Variable can be accessed only inside the class or by its Child class.
But python will allow user to access at any level similar to Global.
So developer have to set their minds not to use them outside the Class.
It declared with single underscode as prefix to variable or method. 
"""
class company():
    def __init__(self,name,age) :
       self.name  = name
       self._age = age
       print(f"Constructor: {self.name} & {self._age}")


c1 = company('Nanban',35)
print(c1.name)  
print(c1._age)  