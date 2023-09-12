# Yuri Conder Roliz Sabbagh
import os
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

bicho1 = Tamagushi('GUTO', 10, 70, 10);
bicho2 = Tamagushi('Rito', 20, 40, 6);
bicho3 = Tamagushi('LUFA', 30, 100, 2);
bicho4 = Tamagushi('MIRO', 40, 90, 5);
bicho5 = Tamagushi('GINO', 50, 80, 3);

lista = [bicho1, bicho2, bicho3, bicho4, bicho5]


#MENU
while True:
    print('---FAZENDA DO TIÃO---')
    print('1-ALIMENTAR BICHOS')
    print('2-BRINCAR COM Os BICHOS')
    print('3-OUVIR BICHOS')
    print('4-CONFERIR STATUS DOS BICHOS')
    print('0-Sair')
    menuInput = int(input('OPÇÃO:'));
    os.system('cls')
    if (menuInput == 0):
        print('Você finalizou o programa');
        break
    if menuInput == 1:
        valor = int(input('Quantidade de comida: '))
        for bicho in lista:
            bicho.set_fome(valor)
    elif menuInput == 2:
        valor = int(input('Tempo em minutos: '))
        for bicho in lista:
            bicho.brincar(valor)
    elif menuInput == 3:
        for bicho in lista:
            print(bicho.get_humor())
    elif menuInput == 4:
        print('---LISTA DE BICHOS---')
        for bicho in lista:
            bicho.__str__()
            print('-------------')
