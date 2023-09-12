#Yuri Conder Roliz Sabbagh

class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome;
        self.fome = fome;
        self.saude = saude;
        self.idade = idade;
        
        # def checarPorcentagem(percent):
        #     if (percent < 100) and (percent > 100):
        #         return 1
        #     else:
        #       return self.set_nome();

    def set_nome(self, nome):
        self.nome = nome;      
      
    def set_fome(self, fome):
        self.fome = fome;
    
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


    def get_humor(self):
        if (((self.get_fome() + self.get_saude())/2) >= 50):
            print(f'{self.get_nome()} está de bom humor :)')
        else:
            print(f'{self.get_nome()} está de mal humor :(')


eletronico = Tamagushi('GUTO',99, 0, 2);

eletronico.get_humor();
            
        