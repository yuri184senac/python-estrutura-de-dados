#OOP Exercise 3: Create a child class Bus that will
# #inherit all of the variables and methods of the Vehicle class

class Velhice:

    def __init__(self, name, max_speed, mileage):
        self.name = name;
        self.max_speed = max_speed;
        self.mileage = mileage;

#Aqui estou herdando a classe Velhice
class Moto(Velhice):
    def __str__(self):
        return f' ---MOTO---\n Nome: {self.name} \n vel max: {self.max_speed} \n milhas:{self.mileage}';

horizon = Moto('Horizon', 150, 3000);

print(horizon)
