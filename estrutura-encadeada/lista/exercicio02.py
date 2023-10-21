class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo
    
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
    
    def __repr__(self):
        return f' {str(self.cabeca)} '

def insereInicio(lista, novo_dado):
    novo_nodo = NodoLista(novo_dado)
    novo_nodo.proximo = lista.cabeca
    lista.cabeca = novo_nodo

def insereDepois(lista, nodo_anterior, novo_dado):
    assert nodo_anterior, "Nodo anterior precisa existir na lista."

    novo_nodo = NodoLista(novo_dado)
    novo_nodo.proximo = nodo_anterior.proximo
    nodo_anterior.proximo = novo_nodo




def removerDuplicatas(lista):
    print('cabeca',lista.cabeca)
    corrente = lista.cabeca
    while corrente:
        proximo_distino = corrente.proximo
        while proximo_distino and proximo_distino.dado == corrente.dado:
            proximo_distino = proximo_distino.proximo
        corrente.proximo = proximo_distino
        corrente = proximo_distino
    return lista


lista = ListaEncadeada()
insereInicio(lista, 10)
insereDepois(lista, lista.cabeca, 10)
insereDepois(lista, lista.cabeca, 20)
print(lista.cabeca)
removerDuplicatas(lista)
