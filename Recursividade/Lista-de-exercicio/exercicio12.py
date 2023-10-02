#12 Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente. 

def imprimirCresc(num1, num2):
  if num1 >= num2:
    return num1
  print(num1,end=',')  
  return imprimirCresc(num1+1, num2)

print(imprimirCresc(1,10)) 
