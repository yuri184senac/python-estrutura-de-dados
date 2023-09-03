class Retangulo:

    def __init__(self, base, altura):
        self.base = base;
        self.altura = altura;

    def mudarValorBase(self, base):
        self.base = base;

    def mudarValorAltura(self, altura):
        self.altura = altura;

    def retornarLados(self):
        return self.base, self.altura;

    def calcularArea(self):
        return self.base * self.altura;

    def calcularPerimetro(self):
        return 2*(self.base) + 2*(self.altura);

#INICIO
print("Informe as medidas para o cálculo da área que serão postos os pisos:");
base = float(input('Largura: '));
altura = float(input('Altura: '));

#OBJETOS
AreaLocal = Retangulo(base,altura);
AreaPiso = Retangulo(4,4);
AreaRodape = Retangulo(1,2);

#Calcular pisos necessários:
qtde_pisos = AreaLocal.calcularArea()/AreaPiso.calcularArea();

#Calcular rodapés necessários:
largura_rodape = AreaRodape.retornarLados();
qtde_rodapes = AreaLocal.calcularPerimetro()/largura_rodape[0] + (largura_rodape[0] * 10 )/100;

print(f'Quantidade de pisos necessários: {round(qtde_pisos)}');
print(f'Quantide de de rodapés necessários: {round(qtde_rodapes)}');









