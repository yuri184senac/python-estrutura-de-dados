#Crie um programa em python que receba um vetor de números reais com 100 elementos. Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor. 
import random

vetorA = []
x = 0;
while x <= 10:
  numero_aleatorio = random.randint(0,100)
  vetorA.append(numero_aleatorio)
  x+=1;

def inverterOrdem(vetor: list, start, end):
  if end <= start:
    return vetor
  aux = vetor[start]
  vetor[start] = vetor[end]
  vetor[end] = aux
    
  return inverterOrdem(vetor, start+1, end-1)

print(vetorA)
print(inverterOrdem(vetorA,0, 10))

