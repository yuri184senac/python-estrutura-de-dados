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

    def remove(self, valor):
        assert self.cabeca, "Impossível remover valor da lista vazia"

        if self.cabeca.dado == valor:
            self.cabeca = NodoLista(valor)
        else:
            anterior = None
            corrente = self.cabeca
            while corrente and corrente.dado != valor:
                anterior = corrente
                corrente = corrente.proximo

            if corrente:
                anterior.proximo = corrente.proximo
            else:
                anterior.proximo = None


lista = ListaEncadeada()

def insereInicio(lista, novo_dado):
    novo_nodo = NodoLista(novo_dado)
    novo_nodo.proximo = lista.cabeca
    lista.cabeca = novo_nodo

def insereDepois(lista, nodo_anterior, novo_dado):
    assert nodo_anterior, "Nodo anterior precisa existir na lista."
    print(nodo_anterior.proximo)
    novo_nodo = NodoLista(novo_dado)
    novo_nodo.proximo = nodo_anterior.proximo
    nodo_anterior.proximo = novo_nodo


lista = ListaEncadeada()
insereInicio(lista, 10)
insereDepois(lista, lista.cabeca, 15)
insereDepois(lista, lista.cabeca, 20)
insereDepois(lista, lista.cabeca, 30)

