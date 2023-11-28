#Yuri Conder Roliz Sabbagh
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


#Exercicio 4
def altura(raiz):
    countEsquerda, countDireita, count = 0,0,0
    if raiz == None:
        return 0
    if raiz.esquerda != None:
        countEsquerda += 1
        countEsquerda += altura(raiz.esquerda)
    if raiz.direita != None:     
     countDireita += 1
     countDireita += altura(raiz.direita)
    count =max(countDireita, countEsquerda)
    return count

#Exercicio 5
def balanceada(raiz):
    if not raiz:
        return True, 0
    esquerda_balanceada, altura_esquerda = balanceada(raiz.esquerda)
    direita_balanceada, altura_direita = balanceada(raiz.direita)

    if not esquerda_balanceada or not direita_balanceada or abs(altura_esquerda - altura_direita) > 1:
        return False, 0

    altura_atual = 1 + max(altura_esquerda, altura_direita)

    return True, altura_atual

#Exercicio 6
def e_simetrica(raiz):
    def e_simetrica_aux(raiz1, raiz2):
        if raiz1 is None and raiz2 is None:
            return True
        if raiz1 is None or raiz2 is None:
            return False

        return (raiz1.chave == raiz2.chave) and \
               e_simetrica_aux(raiz1.esquerda, raiz2.direita) and \
               e_simetrica_aux(raiz1.direita, raiz2.esquerda)

    if raiz is None:
        return True

    return e_simetrica_aux(raiz.esquerda, raiz.direita)


# Cria a árvore 1
raiz = NodoArvore(40)
raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)
raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)
raiz.esquerda.direita.direita = NodoArvore(31)


# Cria a arvore 2 (identica)
raiz2 = NodoArvore(40)
raiz2.esquerda = NodoArvore(20)
raiz2.direita = NodoArvore(60)
raiz2.direita.esquerda = NodoArvore(50)
raiz2.direita.direita = NodoArvore(70)
raiz2.esquerda.esquerda = NodoArvore(10)
raiz2.esquerda.direita = NodoArvore(30)
raiz2.esquerda.direita.direita = NodoArvore(31)


# Cria a arvore 3 (diferente)
raiz3 = NodoArvore(40)
raiz3.esquerda = NodoArvore(20)
raiz3.direita = NodoArvore(60)
raiz3.direita.esquerda = NodoArvore(50)
raiz3.direita.direita = NodoArvore(70)
raiz3.esquerda.esquerda = NodoArvore(10)
raiz3.esquerda.direita = NodoArvore(30)
raiz2.esquerda.direita.direita = NodoArvore(31)

#m_ordem(raiz)

#Questão 01
print("Menor raiz:")
achar_menor(raiz)

#Questão 02
print("Maior raiz:")
achar_maior(raiz)

#Questão 03
print("São iguais:", identicos(raiz, raiz2))

#Questão 04
print("Altura:")
print(altura(raiz))

#Questão 05
# Verifica se a árvore é balanceada
balanceada, altura_arvore = balanceada(raiz)
if balanceada:
    print("A árvore é balanceada.")
else:
    print("A árvore não é balanceada.")


#Questão 06
#Verifica se a árvore é simetrica
print('Arvore simetrica ?')
print(e_simetrica(raiz))