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
     self.count = 0;
  
  def insere(self, novo_dado):
        #Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)
        
        # Faz com que o novo nodo seja o topo da pilha
        novo_nodo.anterior = self.topo
        
        #Faz com que a cabeça da lista referencia o novo nodo.
        self.topo = novo_nodo
        self.count +=1
        pass
    
  
  def remove(self):
        assert self.topo, "Impossível remover o valor da pilha"       
        pop = self.topo.dado
        self.topo = self.topo.anterior
        return pop

     
  
  def __repr__(self):
       return "[" + str(self.topo) + "]"


inteiro = [-1,3,-5,6,0,-10,11,1,-17,21,35,-40,51,-60,63]
   
pilhaP = Pilha()
pilhaN = Pilha()

def tPilha2(vetor):
    for i in vetor:
        if (i > 0):
          pilhaP.insere(i)
        elif (i < 0 ):
          pilhaN.insere(i)
        elif (i == 0):
            pilhaP.remove()
            pilhaN.remove()
          

tPilha2(inteiro)
