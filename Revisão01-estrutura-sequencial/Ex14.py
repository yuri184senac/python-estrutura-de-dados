# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multao valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

print('FISCALIZADOR');

pesoLimiteKg = 50;
pesoPescado = int(input('Quantos quilos de peixe você pescou ?'));

if (pesoPescado > pesoLimiteKg):
    sobrecarga = pesoPescado - pesoLimiteKg;
    multa = sobrecarga * 4.00;
    print(f'Peso permitido {pesoLimiteKg} Kg');
    print(f'Peso excedente do permitido {sobrecarga} Kg');
    print(f'Valor da multa R${multa:0.2f}');

