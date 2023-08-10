#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print('Programa que calcula a área de um quadrado');

lado = float(input('Insira o valor do lado do quadrado:'));

area = lado**2

print(f'O valor da área do quadrado é {area:0.0f} e o dobro da sua área é {2*area:0.0f}');
