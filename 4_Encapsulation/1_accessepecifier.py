## Learn Private Variable
"""
1.Private Variable/Method Cannot be accessed outside the Class.
    Eg:No Attribute Found Error
2.Private Variable/Method cannot be accessed by Child Class also.
3.Private Variable/Method cannot be modified outside the class.
4.Private using __underscode as prefix.

Accessing private Members
    1.Create public Method to access private method.
    2.Use Name mangling
        Syntax: obj._{className}__{functionName}


# """
# Example1:

# class Company:
#     def __init__(self,name,age) :
#        self.name  = name
#        self.__age = age
#        print(f"Constructor: {self.name} & {self.__age}")


# c1 = Company('Python',25)
# print(c1.name)  # Python
# print(c1.__age) # No Attribute error



# # Example 2:
# class Company:
#     def __init__(self,name,age) :
#        self.name  = name
#        self.__age = age
#        print(f"Constructor: {self.name} & {self.__age}")


# class Employee(Company):
#     pass

# emp = Employee("Ganesh",20) 
# print('Emp Name',emp.name) # Emp Name Ganesh
# print('Emp Age',emp.__age) # Error



# class Company:
#     def __init__(self,name,age) :
#        self.name  = name
#        self.__age = age
#        print(f"Constructor: {self.name} & {self.__age}")


# c1 = Company('Python',25)
# c1.name = "Java"
# c1.__age = 50
# print(c1.name) 
# print(c1.__age) 















# Example 3: Mangling method
# class Company:
#     def __init__(self,name,age) :
#        self.name  = name
#        self.__age = age
#        print(f"Constructor: {self.name} & {self.__age}")


# obj = Company("ganesh",75)
# print(obj.name)
# print(obj._Company__age)



# example 4: Using Public Method
class Company:
    def __init__(self,name,age) :
       self.name  = name
       self.__age = age
       print(f"Constructor: {self.name} & {self.__age}")
    
    def showvariables(self):
        print(f"Name is {self.name} & Age is {self.__age} ")

obj = Company("ganesh",23)
print(obj.name)
print(obj.showvariables())