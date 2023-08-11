#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

print('---PROGRAMA QUE CONVERTE GRAUS C EM F')
gCelsius = float(input('Insira uma temperatura em C: '));
gFaren = (9*gCelsius + 160)/5
print(f'{gCelsius}C equivale à {gFaren}F');
