#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9).

print('PROGRAMA CONVERSOR Farenheit para Celsius-');
print('')

gFaren = float(input('Infome a temperatura em Farenheit:'));
celsius = 5*(gFaren-32)/9;

print(f'{gFaren}F equivale à {celsius}C');
