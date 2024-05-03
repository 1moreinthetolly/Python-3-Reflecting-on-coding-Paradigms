# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
  
    def boost(self):
        self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
  
    def flame_jet(self,other):
        other.condition = "trashed"

  
pod = Podracer(100, "wrecked", 1500)
pod.repair()
print("Pod Condition after repair:", pod.condition)

new_pod = AnakinsPod(2, "perfect", 500)
new_pod.boost()
print("Anakin's Pod Max Speed after boost:", new_pod.max_speed)


third_pod = SebulbasPod(150, "perfect", 800)
third_pod.flame_jet(new_pod)
print("Anakin's Pod Condition after flame jet:", new_pod.condition)





'''
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
  *Encapsulation: The classes encapsulate data and behavior. Each class defines its attributes and methods which operate on those attributes.
  *Inheritance: The classes inherit from the base class. They inherit its attributes and methods and can also have their own unique attributes and methods.
  *Polymorphism allows objects of different classes to be treated as objects of a common superclass.
  *Abstraction is the concept of hiding complex implementation details and exposing only essential features of an object. 

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
  *It's subjective whether it would be easier to implement this solution using a different coding style, however, OOP effectively organizes the code into classes and methods, making it readable and maintainable. 

How in particular did Object Oriented Programming assist in the solving of this problem?
  *OOP provided a clear and intuitive approach to solving the problem of organizing and managing podracer inventory. By defining classes, the code represents real-world entities and their behaviors in a structured manner.
'''