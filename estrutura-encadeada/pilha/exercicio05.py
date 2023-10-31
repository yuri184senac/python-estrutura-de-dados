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
   
inteiro = [1,3,5,6,8,10,11,15,17,21,35,40,51,60,63]
   
def tPilha(vetor):
    pilha = Pilha()
    for i in vetor:
        if (i%2 == 0):
            pilha.insere(i)
        elif (i%2 !=1 ):
            pilha.remove()

tPilha(inteiro)

def contarElementos(pilha):
    if pilha.topo != None