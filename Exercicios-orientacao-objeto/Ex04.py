class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def setNome(self, nome):
        self.nome = nome

    def envelhecer(self, maisIdade):
        if (maisIdade < 0):
            print('Não existe idade negativa')
            return None

        #REGRA DE NEGÓCIO: IDADE MENOR QUE 21. A pessoa cresce 5Cm a cada ano envelhecida.
        if self.idade < 21:
            idadeNova = self.idade + maisIdade
            if idadeNova < 21:
                self.crescer(maisIdade * 0.05)
            else:
                self.crescer((idadeNova - 21) * 0.05)

    def engordar(self, maisPeso):
        if (maisPeso < 0):
            print('Não existe peso negativo')
            return
        self.peso = self.peso + maisPeso

    def emagrecer(self, menosPeso):
        self.peso = self.peso - menosPeso

    def crescer(self, maisAltura):
        self.altura = self.altura + maisAltura

    def getAltura(self):
        return self.altura

    def getPeso(self):
        return self.peso

    def getIdade(self):
        return self.idade

    def getNome(self):
        return self.nome

humano = Pessoa('Yuri', 10, 80, 1.00)

print(humano.getAltura())
humano.envelhecer(3)
print(humano.getAltura())
