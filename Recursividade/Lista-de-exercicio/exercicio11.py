 #A multiplicação de dois números inteiros pode ser feita através de somas sucessivas. Proponha um algoritmo recursivo Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros. 

def multip_Rec(n1,n2):
  if n2 <= 1:
    return n1
  return multip_Rec(n1,n2-1)+n1;

print(multip_Rec(5,3)) #SAÍDA:15 pois 5+5+5=15