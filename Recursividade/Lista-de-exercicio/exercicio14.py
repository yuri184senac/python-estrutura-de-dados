#14) Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente. 

def imprimirCrescPar(num1, num2):
  if num1 >= num2:
    return num1
  if num1 % 2 == 0:  
    print(num1,end=',')  
  return imprimirCrescPar(num1+1, num2)

print(imprimirCrescPar(1,10)) 