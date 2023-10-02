#13) Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente
def imprimirDesc(numero):
  if numero <= 1:
    return 1
  print(numero,end=',')  
  return imprimirDesc(numero-1)

print(imprimirDesc(10))
