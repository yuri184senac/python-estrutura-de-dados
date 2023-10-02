#9) Crie uma função recursiva que receba um número inteiro positivo N e calcule o produtório dos números de 1 a N. 

def produtoNumero(n):
    if ( n==1 ):
        return n
    return produtoNumero(n - 1) * n

print(produtoNumero(4))