#15) Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente. 

def imprimirDescPar(numero):
  if numero <= 2:
    return numero
  if numero % 2 == 0:  
    print(numero,end=',')  
  return imprimirDescPar(numero-1)

print(imprimirDescPar(10))