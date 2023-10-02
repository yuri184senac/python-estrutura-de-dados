#3) Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321 

def inverte(num, aux=0):   
  resultado = num // 100; #1
  resto = num % 100 #23
  resultado2 = resto // 10
  resto2 = resto % 10
  final  = str(resto2) + str(resultado2)  + str(resultado);
  return final
print(inverte(123))

def inverte2(num, divisor):
   if 



