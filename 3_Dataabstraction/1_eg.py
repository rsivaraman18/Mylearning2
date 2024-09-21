
"""
    1.Abstract Class and Abstract Method are imported from abc
        Eg: from abc import ABC , abstractmethod
    2.To define an abstract class, it must have at least one method decorated with @abstractmethod. 
       Without it, the class won’t be considered abstract.
    3.To create an abstract class, the class must inherit from the ABC class from the abc module.

    4.All abstract methods in the parent class must be implemented(present) in the subclass. 
      Failing to do so will result in an error "Can't instantiate abstract clas "

    5. If the abstract method is implemented in the subclass, you can call it using super() from that subclass.

    6.An abstract class cannot be instantiated directly. 
      Attempting to create an instance of an abstract class will raise a TypeError. 
      This is because the class is meant to serve as a blueprint for other classes, not to be used directly.

    7.An abstract class can contain concrete (non-abstract) methods with complete functionality.
      Subclasses can inherit and use these methods without the need to override them. 
      Only abstract methods need to be implemented in the subclass.
    8.Multiple Inheritance with Abstract Classes.
"""

# from abc import ABC,abstractmethod
# class Car(ABC):

#     @abstractmethod
#     def movebackward(self):
#         print('Move back')
    
#     @abstractmethod
#     def moveforward(self):
#         print('Move Forward')

#     @abstractmethod
#     def fm(self):
#         print('FM play')
    
#     def gears(self):
#         print('this is normal method ,so it is optional for child class to have this method')

# class Swift(Car):
#     # def movebackward(self):
#     #     print("Swift car moves backward")
        

#     def moveforward(self):
#         print("Swift car moves forward")

#     def fm(self):
#         print("Swift car FM playing")

# # obj = Swift()
# # obj.movebackward()
# # obj.gears()

# # obj = Car()

# obj = Swift()


# Example3


from abc import ABC,abstractmethod
class Car(ABC):

    def movebackward(self):
        print('Move back')

class Swift(Car):
    def movebackward(self):
        print("Swift car moves backward")
        
    
obj = Swift()
obj.movebackward()





