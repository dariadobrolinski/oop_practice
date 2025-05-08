import sys
import stdio
from pet import Pet

def main():
    pets = []

    while not stdio.isEmpty():
        name = stdio.readString()
        species = stdio.readString()
        age = stdio.readInt()
        weight = stdio.readInt()

        new_pet = Pet(name, species, age, weight)

        for pet in pets:
            if pet == new_pet:
                pet._weight += 5
                pet._age += 2   
                break
            else: 
                pets.append(new_pet)

    print("All Pets:")
    for pet in pets:
        print(pet)

    print("\nAdoptable Pets:")
    for pet in pets:
        if pet.isAdoptable():
            print(pet)

    if pets:
        lightest = min(pets, key=lambda p: p.getWeight())
        print("\nLightest Pet:")
        print(lightest)

if __name__ == '__main__':
    main()