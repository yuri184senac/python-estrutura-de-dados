class Nodo:
    """Esta classe representa um nodo de uma estrtura duplamente encadeada."""
    
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado;
        self.proximo = proximo_nodo;
        
    def __repr__(self):
        return '% -> %s' % (self.dado, self.proximo) 
    

class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada."""
    
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    
    def insere(self, novo_dado):
        """Insere um elemento no final da fila."""
    
        #Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)
        
        #Insere em uma fila vazia
        if self.primeiro == None:
            
    def __repr__(self):
        return "["+ str(self.primeiro) + "]"
    
    
    