#Grupo: JOSÉ PAULO SAPPI, LUIS FERNANDO IUNES ABRAHÃO, YURI CONDER ROLIZ SABBAGH

#2) Implemente uma função recursiva para calcular 1 + 1/2 + 1/3 + 1/4 + ... + 1/N .
from fractions import Fraction
def calcular(n):
    if n == 1:
        return 1ffsfsf
    return Fraction(1, n) + calcular(n-1)

print(calcular(3))