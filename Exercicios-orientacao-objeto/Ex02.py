class Quadrado:
    
    def __init__(self, lado):
        self.lado = lado;

    def mudarValorLado(self, lado):
        self.lado = lado;

    def getValorLado(self):
        return self.lado;

    def calcularArea(self):
        return self.getValorLado() ** 2;

quadrado = Quadrado(4);

print(quadrado.getValorLado());
print(quadrado.calcularArea());

quadrado.mudarValorLado(6);
print(quadrado.calcularArea());
        