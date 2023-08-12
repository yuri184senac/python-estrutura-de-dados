# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
print('PROGRAMA QUE PEDE 2 NÚMEROS INTEIRO E UM NÚMERO REAL');
n = float(input('Insira um número REAL: '));
n2 = int(input('Insira um número inteiro:'));
n3 = int(input('Insira outro número inteiro:'));

produto = (2*n*n2/2);
soma = 3*n + n3;

print(f'produto: {produto}');
print(f'soma: {soma}');
print(f'{n3}^3={n3**3}');

