#Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N.

def calculaFatorial(numero):
    if (numero <= 1):
        return numero
    return calculaFatorial(numero-1)*numero;


print(calculaFatorial(7))

