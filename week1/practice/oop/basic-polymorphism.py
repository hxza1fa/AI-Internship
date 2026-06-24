class Animal:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        print("Animal noises...")

class Dog(Animal):
    def speak(self):
        print("Woof woof")

class Cat(Animal):
    def speak(self):
        print("Meow Meow")

def main():
    cat1 = Cat("Billy", 2, "Siamese")
    cat2 = Cat("Johnny", 3, "Orange")

    dog1 = Dog("Henry", 7, "Pitbull")
    dog2 = Dog("Galaxy Destroyer", 1, "Poodle")

    animal1 = Animal("Random Animal", 10, "Random species")

    all_animals = [cat1, cat2, dog1, animal1, dog2]

    for a in all_animals:
        a.speak()

if __name__ == "__main__":
    main()