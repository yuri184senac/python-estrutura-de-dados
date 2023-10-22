#1. Escrever uma função que receba como parâmetro uma pilha. A função deve retornar o maior elemento da pilha.
class Pilha:
  def __init__(self):
    self.item = []
    self.count = 0
  def adicionar(self, element):
    self.item.append(element)
    self.count+=1
  def __repr__(self):
      return f' {str(self.item)} '
    
p = Pilha()
p.adicionar(2)
p.adicionar(3)
p.adicionar(10)
p.adicionar(7)

def retornarUltimoElemento(pilha):
   for i in range(pilha.count):
      if i+1 == pilha.count:
        return pilha.item[i]

print(retornarUltimoElemento(p))




