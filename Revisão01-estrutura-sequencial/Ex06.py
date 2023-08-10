#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
print('Programa que calcula a área de um círculo');

raio = float(input('Informe a o raio do círculo:'));

area = (raio**2) * 3.14;
print(f'A área do círculo de raio {raio} é igual a: {area:0.2f}cm2');
