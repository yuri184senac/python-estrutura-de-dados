#10) Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N. Por exemplo, o dígito 2 ocorre 3 vezes em 762021192. 

def contarDigito(num, dig, pos, contador=0):
  if  pos < 1:  
    return contador;
  numString = str(num)
  if (numString[pos-1] == str(dig)):
   contador+=1;
  return contarDigito(num, dig, pos-1, contador) ;

numero = 762021192;
print('Número de repetições:',contarDigito (numero, 2, len( str(numero) )));