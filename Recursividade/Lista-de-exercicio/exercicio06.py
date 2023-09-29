#Crie um programa em python, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule k^n . Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função. 

k = int(input('Insira valor de k: '));
n = int(input('Insira valor de n: '));


def potencia(k,n):
    if (n==1):
        return k
    elif (n==0):
        return 1
    return potencia(k,n-1)*k

print(potencia(k,n))


