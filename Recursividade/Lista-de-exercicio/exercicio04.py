#Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.

def soma(vetor):
    if vetor == []:
        return 0;
    return vetor[0] + soma(vetor[1:])

vetorA = [1,2,3,4,5]
print(soma(vetorA))