#Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.

def soma(vetor):
    if not vetor == []:
        return vetor;
    return soma(vetor[0]+vetor[1:])

vetorA = [1,2,3,4,5]
print(soma(vetorA))