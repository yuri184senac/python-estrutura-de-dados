#Faça um Programa que peça dois números e imprima a soma.
num1 = 0
num2 = 0

while (num1%2 == 0) and (num2%2 == 0):
    num1 = int(input('Insira um número ímpar:'));
    num2 = int(input('Insira outro número ímpar:'));
    print('Número inserido é par, tente outra vez!');
    
print(f'A soma dos números inseridos {num1}+{num2}={num1+num2}');