# 4. Construa um programa utilizando uma pilha que resolva o seguinte problema: 
# Armazene as placas dos carros (apenas os números) que estão estacionados numa rua sem saída estreita. 
# Dado uma placa verifique se o carro está estacionado na rua. 
# Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair.


class Nodo:
    """Esta classe representa um nodo de uma estrutura."""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior
        
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

class Pilha:
  def __init__(self):
     self.topo = None
     self.count = 0 
  def insere(self, novo_dado):
        #Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)
        
        # Faz com que o novo nodo seja o topo da pilha
        novo_nodo.anterior = self.topo
        
        #Faz com que a cabeça da lista referencia o novo nodo.
        self.topo = novo_nodo
        self.count+=1
        pass
    
  
  def remove(self):
        assert self.topo, "Impossível remover o valor da pilha"       
        pop = self.topo.dado
        self.topo = self.topo.anterior
        return pop

  def verificarCarros(self, placa):
      temp = self.topo
      carros_retirados = []

      while temp:
          if temp.dado == placa:
              break
          carros_retirados.append(temp.dado)
          temp = temp.anterior

      if not temp:
          return "Carro não encontrado na rua."

      self.topo = temp.anterior
      carros_retirados.reverse()
      return carros_retirados

  def __repr__(self):
       return "[" + str(self.topo) + "]"
  
 
estacionamento = Pilha()

estacionamento.insere('1234')
estacionamento.insere('4234')
estacionamento.insere('5234')
estacionamento.insere('6234')

print(estacionamento.verificarCarros('5234'))