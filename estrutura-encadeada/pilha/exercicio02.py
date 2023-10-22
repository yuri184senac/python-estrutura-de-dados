# 2. Utilizando uma pilha resolver o exercício a seguir: Dada uma sequência contendo N (N >0) números reais, imprimi-la na ordem inversa.

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
  
  def insere(self, novo_dado):
        #Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)
        
        # Faz com que o novo nodo seja o topo da pilha
        novo_nodo.anterior = self.topo
        
        #Faz com que a cabeça da lista referencia o novo nodo.
        self.topo = novo_nodo
        pass
    
  
  def remove(self):
        assert self.topo, "Impossível remover o valor da pilha"       
        pop = self.topo.dado
        self.topo = self.topo.anterior
        return pop

     
  
  def __repr__(self):
       return "[" + str(self.topo) + "]"
  

listaSequencial = [1,3,5,7,11,13,17,19,23]
listaInvertida = []
p = Pilha()
p_invertida = Pilha()

for i in listaSequencial:
   p.insere(i)
print('Pilha Normal: ', p)

for i in range(len(listaSequencial)):
   p_invertida.insere(p.remove())


print('Pilha invertida: ',p_invertida)



