class Retangulo:
    
    def __init__(self, base, altura):
        self.base = base;
        self.altura = altura;

    def mudarValorBase(self, base):
        self.base = base;

    def mudarValorAltura(self, altura):
        self.altura = altura;

    def retornarLados(self):
        return [self.altura, self.base]

    def calcularArea(self): 
        return self.base * self.altura;

    def calcularPerimetro(self):
        return 2*(self.base) + 2*(self.altura);

      
base = float(input('Largura: '));
altura = float(input('Altura: '));

AreaLocal = Retangulo(base,altura);
AreaPiso = Retangulo(4,4);

#Calcular pisos necessários:
qtde_pisos = AreaLocal.calcularArea()/AreaPiso.calcularArea();

print(qtde_pisos)





        

        