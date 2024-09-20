# Many methods with same name but with differnt params in a Particular class

class Example:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"Two arguments: {a} and {b}")
        elif a is not None:
            print(f"One argument: {a}")
        else:
            print("No arguments")

# Usage
obj = Example()
obj.display()           # No arguments
obj.display(10)         # One argument
obj.display(10, 20)     # Two arguments
