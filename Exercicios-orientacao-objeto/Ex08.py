class Macaco:
  def __init__(self, nome, bucho):
    self.nome = nome;
    self.bucho = bucho;

  def comer(self, alimento):
    self.bucho = alimento;

  def __str__(self) -> str:
     return f'Macaco(a){self.nome} está satisfeito em comer {self.bucho}';


macaco_1 = Macaco('Jose', 'banana');
macaco_2 = Macaco('Gigante', macaco_1.nome);

print(macaco_1)
print(macaco_2);

#Sim! é possível criar uma macaco canibal