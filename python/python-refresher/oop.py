class ChaiOrder:
  def __init__(self, type_, size):
    self.type = type_
    self.size = size
  def summary(self):
    return f"{self.size}ml of {self.type} chai"
  
order = ChaiOrder("masala", 250)
print(order.summary())

# Inheritance
class BaseChai:
  def __init__(self, type_): # __init__ constructor
    self.type = type_
  
  def prepare(self):
    return f"Preparing {self.type} chai...."

# Inheriting from BaseChai
class MilkChai(BaseChai): # inherit BaseChai class
  def add_spices(self):
    print("Adding cardamom, ginger, cloves.")

# Composition example
class ChaiShop:
  chai_cls = BaseChai # inheritance all the values of this base chai
  def __init__(self):
    self.chai = self.chai_cls("Regular") # Composition of Chai class
  def serve_chai(self):
    print(f"Serving {self.chai.type} chai in the shop")
    self.chai.prepare()
  
class FancyChaiShop(ChaiShop):
  chai_cls = MilkChai


# creating some objects
shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve_chai()
fancy.serve_chai()
fancy.chai.add_spices()


## 3 ways to access Base Class
class Coffee:
  def __init__(self, type_, strength):
    self.type = type_
    self.strength = strength
  

class Espresso(Coffee):
  def __init__(self, type_, strength, size):
    # Coffee.__init__(type_, strength)  # explicitly calling the base class constructor
    super().__init__(type_, strength)  # Method 1: Using super()
    self.size = size
  
  def summary(self):
    return f"{self.size}ml {self.type} espresso with {self.strength} strength"