class Nodo:
    """Esta classe representa um nodo de uma estrutura."""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior
        
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)
    
    
class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada."""
    
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
    
    def __repr__(self):
        return "[" + str(self.topo) + "]"
    

#INICIO


stack = Pilha() #A pilha começa vazia, o topo=None. Ninguém está no topo quando a pilha é inicializada
stack.insere(5) #O que é inserido na pilha é o nodo. O nodo armazena um valor e um endereço de memória
stack.insere(6)
stack.insere(7)
print(stack)