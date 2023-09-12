# Yuri Conder Roliz Sabbagh

# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    
    def __init__(self, cor, circuferencia, material):
        self.cor = cor;
        self.circuferencia = circuferencia;
        self.material = material;


    def trocarCor(self, cor) :
      self.cor = cor;
    

    def mostrarCor(self):
       return self.cor


bola = Bola('azul', 30, 'borracha')

print(bola.mostrarCor());
bola.trocarCor('preto');
print(bola.mostrarCor());

  
  
        
        
        
