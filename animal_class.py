import random

class Animal:
  """A generic animal"""

  #constructor
  def __init__(self,name,growth_rate,food_need,water_need):
    #set the attributes with an initial value

    self._weight = 0
    self._days_growing = 0
    self._growth_rate = growth_rate
    self._food_need = food_need 
    self._water_need = water_need
    self._status = "Baby"
    self._type = "Generic"
    self._name = name

  #adding the needs method
  def needs(self):
    #returns a dictionary containing food and water needs
    return {"food need":self._food_need, "water need":self._water_need}

  #method to report the provided information about the crops current status
  def report(self):
    #returns a dictionary containing the type, status, growth and days gowing
    return {"type":self._type,"status":self._status,"name":self._name,"weight":self._weight,"days growing":self._days_growing}
    print()
    print(name)
  def _update_status(self):
    if self._weight > 15:
      self._status = "Old"
    elif self._weight > 10:
      self._status = "Mature"
    elif self._weight > 5:
      self._status = "Teen"
    elif self._weight > 0:
      self._status = "Young"
    elif self._weight == 0:
      self._status = "Baby"

  def grow(self,food,water):
    if food >= self._food_need and water >= self._water_need:
      self._weight += self._growth_rate
    #increment the number of days growing
      self._days_growing += 1
    #update status
      self._update_status()


def auto_grow(animal, days):
  #grow the animal
  for day in range(days):
    food = random.randint(1,10)
    water = random.randint(1,10)
    animal.grow(food,water)

def manual_grow(animal):
  #get the food and water values from the user
  valid = False
  while not valid:
    try:
      food = int(input("Please enter a food value (1-10): "))
      if 1<= food <=10:
        valid = True
      else:
        print("Value entered not valid - please enter a value between 1 and 10")
    except ValueError:
      print("Value entered not valid - please enter a value between 1 and 10")
  valid = False
  while not valid:
    try:
      water = int(input("Please enter a water value (1-10): "))
      if 1<= water <=10:
        valid = True
      else:
        print("Value entered not valid - please enter a value between 1 and 10")
    except ValueError:
      print("Value entered not valid - please enter a value between 1 and 10")
  #grow the crop
  animal.grow(food,water)
def get_name():
    valid = False
    while not valid:
        name = input("Please enter a name for the animal: ")
        if len(name) > 0:
            valid = True
        else:
            print("Error! You need to enter a name for the cow")
    return name

def display_menu():
  print("1. Grow manually over 1 day")
  print("2. Grow automatically over 30 days")
  print("3. Report status")
  print("0. Exit test program")
  print()
  print("Please select an option from the above menu")

def get_menu_choice():
  option_valid = False
  while not option_valid:
    try:
      choice = int(input("Option Selected: "))
      if 0 <= choice <= 4:
        option_valid = True
      else:
        print("Please enter a valid option")
    except ValueError:
      print("Please enter a valid option")
  return choice

def manage_animal(animal):
  print("This is the animal management program")
  print()
  noexit = True
  while noexit:
    display_menu()
    option = get_menu_choice()
    print()
    if option == 1:
      manual_grow(animal)
      print()
    elif option == 2:
      auto_grow(animal,30)
      print()
    elif option == 3:
      print(animal.report())
      print()
    elif option == 0:
      noexit = False
      print()
  print("Thank you for using the crop management program")


def main():
  #instantiate the class
  name = get_name()
  new_animal = Animal(name,1,3,3)
  manage_animal(new_animal)
  print(name)
  

if __name__ == "__main__":
  main()
