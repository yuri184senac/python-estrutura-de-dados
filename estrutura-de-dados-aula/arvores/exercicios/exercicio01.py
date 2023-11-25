class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def _repr_(self):
        return '%s <- %s -> %s' % (
        self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)


def em_ordem(raiz):
    if not raiz:
        return

    # Visita filho da esquerda.
    em_ordem(raiz.esquerda)

    # Visita nodo corrente.
    print(raiz.chave),

    # Visita filho da direita.
    em_ordem(raiz.direita)


# Exercicio 1 - Encontre o menor elemento em uma BST.

def achar_menor(raiz):
    if raiz.esquerda == None:
        print(raiz.chave)

    else:
        raiz = raiz.esquerda
        achar_menor(raiz)


# Exercicio 2 - Encontre o maior elemento em uma BST.
def achar_maior(raiz):
    if raiz.direita == None:
        print(raiz.chave)

    else:
        raiz = raiz.direita
        achar_maior(raiz)


# Exercicio 3 - Verifique se duas árvores binárias são idênticas.
#Essa aqui só identifica se a árvore possui o mesmo tamanho
def identicos(a: NodoArvore, b: NodoArvore):
    if (a == None and b == None):
        return True;

    if (a != None and b != None):
        return (
                identicos(a.esquerda, b.esquerda) and identicos(a.direita, b.direita)
                )
    return False

def altura(raiz):
    count = 0
    if raiz == None:
        return 0
    elif(raiz.esquerda != None or raiz.direita != None):
        count += 1
        count += altura(raiz.esquerda)
        count += altura(raiz.direita)
    return count




# Cria a arvore 1
raiz = NodoArvore(40)
raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)
raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)

print(altura(raiz))

# Cria a arvore 2 (identica)
raiz2 = NodoArvore(40)

raiz2.esquerda = NodoArvore(20)
raiz2.direita = NodoArvore(60)

raiz2.direita.esquerda = NodoArvore(50)
raiz2.direita.direita = NodoArvore(70)
raiz2.esquerda.esquerda = NodoArvore(10)
raiz2.esquerda.direita = NodoArvore(30)

# Cria a arvore 3 (diferente)
raiz3 = NodoArvore(40)

raiz3.esquerda = NodoArvore(20)
raiz3.direita = NodoArvore(60)

raiz3.direita.esquerda = NodoArvore(50)
raiz3.direita.direita = NodoArvore(70)
raiz3.esquerda.esquerda = NodoArvore(5)
raiz3.esquerda.direita = NodoArvore(32)


#m_ordem(raiz)

#Questão 01
#achar_menor(raiz)

#Questão 02
#achar_maior(raiz)

#Questão 03
#print(identicos(raiz, raiz3))
