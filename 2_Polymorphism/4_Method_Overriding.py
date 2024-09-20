"""
Method Overridding: It is possible only with Inheritance.
                    Here the method with same params have to present in both the class

"""
class Father:
    def sleep(self):
        print("Sleeps at 8 pm")

    def eats(self):
        print("He cooks and eat")

class Son(Father):
    def sleep(self):
        super().sleep()

person = Son()
person.eats()
person.sleep()