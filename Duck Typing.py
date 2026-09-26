# Duck Typing --- Another way to acheive polymorphism besides Inheritance. Object must have the minimum necessary
#                   attributes/methods 

class Animal:
    alive = True

class Tiger(Animal):
    def speak(self):
        print("ROAR!")

class Horse(Animal):
    def speak(self):
        print("NEIGH!")

class Car:
    alive = False
    def speak(self):
        print("HONK!")

animals = [Tiger(), Horse(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)