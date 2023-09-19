#Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.

vetorA = [1,2,3,4,5]


def soma(vetor):
    print(vetor)
    if (len(vetor)==1):
        return vetor;
    return soma(vetor[4])

print(soma(vetorA))