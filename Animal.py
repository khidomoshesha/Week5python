class Animal:
    def move(self):
        print("Generic animal movement.")

class Dog(Animal):
    def move(self):
        print("Running on four legs.")

class Bird(Animal):
    def move(self):
        print("Flying through the air.")

class Fish(Animal):
    def move(self):
        print("Swimming in the water.")

# Creating a list of different animal objects
animals = [Dog(), Bird(), Fish()]

# Calling the move() method on each animal
for animal in animals:
    animal.move()