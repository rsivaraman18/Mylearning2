### Data Abstraction

class Bike:
    def __init__(self):
        self.tyres = 2

    def start(self):
        return "Start with kicker"
    
class Scooty:
    def __init__(self):
        self.tyres = 2

    def start(self):
        return "Self Start"
    
class Car:
    def __init__(self):
        self.tyres = 4
        
    def start(self):
        return "Start the car with Key"

