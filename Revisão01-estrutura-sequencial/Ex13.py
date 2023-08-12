#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

escolha=0;
print('PESO IDEAL');
print('----------');
print('SELECIONE O SEU SEXO:');
print('1-Homem');
print('2-Mulher');

while(escolha != 1 and escolha != 2):
  escolha = int(input('Digite a opção desejada: '));    

h = float(input('Insira a sua altura: '));

if(escolha == 1):
  print(f'O seu peso ideal é {(72.7*h)-58}');
elif(escolha == 2):
  print(f'O seu peso ideal é {(62.1*h)-44.7}');
