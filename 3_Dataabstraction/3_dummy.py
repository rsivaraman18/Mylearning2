from abc import ABC,abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def some_method(self):
        pass

    def normal_method(self):
        print("This is a normal method in the base class")

class ChildClass(BaseClass):
    def some_method(self):
        print("Abstract method implemented in child class")
    
    def use_super(self):
        super().normal_method()  # Calling the normal method from the parent class
        super().some_method()    # Not typical, but possible after implementing it

child = ChildClass()
child.use_super()
