# Yuri Conder Roliz Sabbagh
class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome;
        self.fome = fome;
        self.saude = saude;
        self.idade = idade;
        self.humor = 0;

    def set_nome(self, nome):
        self.nome = nome;

    def set_fome(self, qtdeComida):
        self.fome += qtdeComida;
        if (qtdeComida > 5):
            maisHumor = 10
        elif (qtdeComida > 4):
            maisHumor = 8
        elif (qtdeComida > 3):
            maisHumor = 6
        elif (qtdeComida > 2):
            maisHumor = 4
        else:
            maisHumor = 2
        self.set_humor(maisHumor)

    def set_saude(self, saude):
        self.saude = saude;

    def set_idade(self, idade):
        self.idade = idade;

    def get_nome(self):
        return self.nome;

    def get_fome(self):
        return self.fome;

    def get_saude(self):
        return self.saude;

    def get_idade(self):
        return self.idade;

    def brincar(self, tempo):
        if (tempo > 120):
            maisHumor = 40
        elif (tempo > 60):
            maisHumor = 30
        elif (tempo > 30):
            maisHumor = 20
        elif (tempo > 15):
            maisHumor = 10
        else:
            maisHumor = 5
        self.set_humor(maisHumor)

    def get_humor(self):
        if (self.humor > 90):
            msg = f'{self.nome} está muito feliz!'
        elif (self.humor > 60):
            msg = f'{self.nome} está feliz!'
        elif (self.humor > 30):
            msg = f'{self.nome} está legal!'
        elif (self.humor > 15):
            msg = f'{self.nome} está chateado!'
        else:
            msg = f'{self.nome} está entediado!'
        return msg

    def set_humor(self, valor):
        if valor < 100 :
            self.humor += valor
        else:
            pass

    def __str__(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Fome: {self.fome}')
        print(f'Saude: {self.saude}')
        print(f'Humor: {self.humor}')





bicho = Tamagushi('GUTO', 10, 100, 2);
print('Características:')
bicho.__str__()

print('--STATUS--')
bicho.set_fome(2)
bicho.brincar(40)
print(bicho.get_humor());
bicho.brincar(120)
print(bicho.get_humor());


