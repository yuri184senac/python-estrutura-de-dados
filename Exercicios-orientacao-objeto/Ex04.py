class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome;
        self.idade = idade;
        self.peso = peso;
        self.altura = altura;

    def setNome(self, nome):
       self.nome = nome;
      
    def envelhecer(self, maisIdade):
      if (maisIdade < 0):
         print('Não existe idade negativa');
         return;
      self.idade = self.idade + maisIdade;

    def engordar(self, maisPeso):
        if (maisPeso < 0):
          print('Não existe peso negativa');
          return;
        self.peso = self.peso + maisPeso;
            
    def emagrecer(self, menosPeso):
       self.peso = self.peso - menosPeso;

    def crescer(self, maisAltura):
       self.altura = self.altura + maisAltura;

    def getAltura(self):
       return self.altura;

    def getPeso(self):
       return self.peso;

    def getIdade(self):
       return self.idade;
        
    def getNome(self):
       return self.nome;

humano = Pessoa('Fulano',20,80,1.75);
print('PRESENTE')
print(humano.getNome());
print(humano.getIdade());
print(humano.getPeso());
print(humano.getAltura());

humano.engordar(1);
humano.envelhecer(5);
humano.emagrecer(10);
humano.crescer(0.2);
humano.setNome('Yuri');

print('FUTURO')
print(humano.getNome());
print(humano.getIdade());
print(humano.getPeso());
print(humano.getAltura());