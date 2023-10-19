#Contexto:
# Um servico de streaming de videos quer implementar a funcionalidade de Loop em suas playlists, para que
# quando o ultimo item da playlist termine, ela reinicie a exibicao a partir do primeiro item da mesma.

#Solução:
# A solução encontrada foi modificar as playlists para que deixem de ser objetos do tipo "Lista simples", e passem a ser
# "listas circulares."
# Assim, o ultimo item da playlist deixará de apontar para a funçao STOP do player, e apontará para o primeiro item
# da playlist, possibilitando a exibição em Loop."""

class Nodo:
    def _init_(self, dado):
        self.dado = dado
        self.proximo = None


class Playlist:
    def _init_(self):
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



if __name__ == "__main__":
    promohub = Playlist()

    promohub.exibir()