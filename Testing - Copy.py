from sheep_class import *
from cow_class import *

def display_menu():
    print()
    print("Which animal would you like to create?")
    print()
    print("1. Sheep")
    print("2. Cow")
    print()
    print("Please enter your choice: ")

def select_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,2):
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice
def create_animal():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_animal = Sheep(Animal)
        name = get_name()
    #create a new cow animal
        new_cow = Sheep(name)
    elif choice == 2:
        name = get_name()
        new_cow = Cow(name)
        new_animal = Cow(Animal)
    return new_animal
            
def main():
    new_animal = create_animal()
    manage_animal(new_animal)
if __name__ == "__main__":
    main()
