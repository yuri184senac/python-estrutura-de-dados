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
        
    def __repr__(self):
        return "[" + str(self.topo) + "]"