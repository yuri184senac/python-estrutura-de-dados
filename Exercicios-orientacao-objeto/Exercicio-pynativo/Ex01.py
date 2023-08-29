#OOP Exercise 1: Create a Class with instance attributes
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes

class Velhice:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed;
        self.mileage = mileage;

    def __str__(self):
        return f'Velocidade máxima: {self.max_speed} \n Milhas: {self.mileage}';

corsa = Velhice(20,40);
print(corsa);


