# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

print('---PROGRAMA---')

sal_hora = int(input('Quanto você ganha por hora R$:'));
hora_trb_mes = int(input('Total de horas trabalhadas no mês: '));
sal_total = sal_hora * hora_trb_mes;

ir = sal_total*(11/100);
inss = sal_total*(8/100);
sindicato = sal_total*(5/100);

desconto = ir + inss + sindicato;

sal_bruto = sal_total;
sal_liquido = sal_bruto - desconto;

print('--CÁLCULO--')
print(f'Salário bruto R${sal_bruto:0.2f}');
print(f'Imposto de renda R${ir:0.2f}');
print(f'INSS R${inss:0.2f}');
print(f'Sindicato R${sindicato:0.2f}');
print(f'Salário líquido R${sal_liquido:0.2f}');