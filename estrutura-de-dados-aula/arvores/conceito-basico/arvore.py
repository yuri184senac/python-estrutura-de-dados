class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave #É o valor do nodo
        self.esquerda = esquerda
        self.direita = direita 
        
    def __repr__(self):
        return '%s <- %s -> %s' % (
                                    self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave
                                  )
        
    

raiz = NodoArvore(40)
raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)
raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)



def em_ordem(raiz):
    if not raiz:
        return
    em_ordem(raiz.esquerda)
    print(raiz.chave) 
    em_ordem(raiz.direita)

# def pre_ordem(raiz):
#     if not raiz:
#         return
#     print(raiz.chave)
#     pre_ordem(raiz.esquerda)
#     pre_ordem(raiz.direita)


em_ordem(raiz)