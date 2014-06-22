from animal_class import *

class Cow(Animal):
    """A generic Sheep"""

    #constructor
    def __init__(self,name):
        #call parent class constructor with default values for potato
        #growth rate = 1; food need = 3; water need = 6
        super().__init__(name,1,3,6)
        self._type = "Cow"

    #overriding grow method for subclass
    def grow(self,food,water):
        if  food >= self._food_need and water >= self._water_need:
            if self._status == "Young" and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == "Calf" and water > self._water_need:
                self._weight += self._growth_rate * 1.25
            else:
                self._weight = self._growth_rate
        #increment the days growing
        self._days_growing += 1
        #update status
        self._update_status()
def main():

    #manually grow the animal
    manual_grow(new_cow)
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())

if __name__ == "__main__":
    main()
