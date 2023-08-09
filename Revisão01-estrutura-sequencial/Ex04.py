#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas= [0,0,0,0];
media = 0;
print('Insira as suas 4 notas bimestrais');

for nota in range(0,4):
    notas[nota] = float(input(f'Insira a sua nota no {nota+1} bimestre:'));
    media = notas[nota] + media;

print(media/4);

