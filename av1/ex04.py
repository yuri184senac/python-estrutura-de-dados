#Grupo: JOSÉ PAULO SAPPI, LUIS FERNANDO IUNES ABRAHÃO, YURI CONDER ROLIZ SABBAGH

#4) Implemente uma lista circular com estrutura encadeada com os seguintes métodos: inserção, remoção e busca.
class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Circular:
    def __init__(self):
        self.cabeca = None


    def inserir(self, dado):
        novo_nodo = Nodo(dado)
        if not self.cabeca:
            self.cabeca =  novo_nodo
            novo_nodo.proximo = self.cabeca
        else:
            corrente = self.cabeca
            while corrente.proximo != self.cabeca:
                corrente = corrente.proximo
            corrente.proximo = novo_nodo
            novo_nodo.proximo = self.cabeca

    def buscar(self,valor):
        if not self.cabeca:
            print ("Lista Vazia")
            return
        corrente = self.cabeca
        while True:
            if corrente.dado == valor:
                print (f"{valor} presente na lista")
                return corrente
            corrente = corrente.proximo
            if corrente == self.cabeca:
                return None



    def remover(self,valor):
        if not self.cabeca:
            return
        corrente = self.cabeca
        anterior = None
        while True:
            if corrente.dado == valor:
                if anterior:
                    anterior.proximo = corrente.proximo
                    if corrente == self.cabeca:
                        self.cabeca = corrente.proximo
                    corrente.proximo = None
                    return
                else:
                    ultimo_nodo = corrente
                    while ultimo_nodo.proximo != self.cabeca:
                        ultimo_nodo = ultimo_nodo.proximo
                    ultimo_nodo.proximo = corrente.proximo
                    self.cabeca = corrente.proximo
                    return
            anterior = corrente
            corrente = corrente.proximo
            if corrente == self.cabeca:
                return

    def exibir(self):
        if self.cabeca is None:
            return "Lista Vazia"
        corrente = self.cabeca
        while True:
            print(corrente.dado, end="->")
            corrente = corrente.proximo
            if corrente == self.cabeca:
                break
        print(" retorna para cabeca")


lista = Circular()
lista.inserir(1)
lista.inserir(2)
lista.inserir(3)

lista.exibir()

lista.buscar(2)

lista.remover(2)
lista.exibir()    