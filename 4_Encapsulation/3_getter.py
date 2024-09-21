class Student:
    def __init__(self,name,roll,age):
        self.name = name
        self._roll = roll
        self.__age = age

    def get_age(self):
        return f"{self.name} age is {self.__age}"
    
    def set_age(self):
        if self.__age >20:
            return self.__age
        else:
            return "You are too young"

obj = Student("Python",1001,20)
print(obj.name) 
print(obj._roll)
print(obj.get_age())
## Set age

print(obj.set_age())
    
