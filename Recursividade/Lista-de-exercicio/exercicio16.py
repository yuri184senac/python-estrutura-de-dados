#16) A função fatorial duplo é definida como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15 Faça uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número.


def calculaFatorialDupla(numero):
    if (numero <= 1):
        return numero
    return calculaFatorialDupla(numero-2)*numero;

print(calculaFatorialDupla(5)) 