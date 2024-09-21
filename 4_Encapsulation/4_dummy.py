class Company:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.__age = age  # Private attribute
        print(f"Constructor: {self.name} & {self.__age}")


c1 = Company('Python', 25)  # Creating an object of Company class
c1.name = "Java"  # Modifying the public variable 'name'
c1.__age = 70     # Trying to modify the private variable '__age'
# print(c1.name)    # This will print 'Java' as it is a public variable
print(c1.__age)   # This will raise an AttributeError
