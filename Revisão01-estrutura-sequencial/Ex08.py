#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print('---PROGRAMA CALCULA SALÁRIO TOTAL DO MÊS---');
print('');

v_salario_hora = float(input('Valor ganhado por hora R$:'));
hora_trab_mes = int(input('Horas trabalhadas pro mês: '));

print(f'Salário total no mês {v_salario_hora * hora_trab_mes}');
