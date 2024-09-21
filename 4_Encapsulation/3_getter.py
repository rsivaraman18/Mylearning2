class Student:
    def __init__(self,name,roll,age):
        self.name = name
        self._roll = roll
        self.__age = age

    def get_age(self):
        return f"{self.name} age is {self.__age}"
    
    def set_age(self,newage):
        if newage > 35:
            print(f"{newage} is Invalid ")
        else:
            self.__age = newage
            

obj = Student("Python",1001,20)
print(obj.name) 
print(obj._roll)
print(obj.get_age())
## Set age
obj.set_age(27)
print(obj.get_age())
    
