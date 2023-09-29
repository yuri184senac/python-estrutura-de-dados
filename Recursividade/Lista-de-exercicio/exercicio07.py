#Crie um programa em python que receba um vetor de números reais com 100 elementos. Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor. 
import random

vetorA = []
x = 0;
while x <= 100:
  numero_aleatorio = random.randint(0,100)
  vetorA.append(numero_aleatorio)
  x+=1;

def inverterOrdem(vetor: list):
  if vetor.index == 0:
    return 1
  return inverterOrdem(vetor[:])


