# Crie uma função recursiva que receba um número inteiro positivo
# N e calcule o somatório dos números de 1 a N.
def calculaSoma(n):
    if (n==1):
        return n
    return calculaSoma(n-1)+n

print(calculaSoma(3))

