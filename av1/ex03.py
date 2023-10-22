#Grupo: JOSÉ PAULO SAPPI, LUIS FERNANDO IUNES ABRAHÃO, YURI CONDER ROLIZ SABBAGH

#3) Implemente uma função recursiva para verificar se uma palavra é palíndromo (Ex. aba, abcba, xyzzyx).
#Definição:  frase ou palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa.

def verificarPalindromo(word1, e=None,  s=0):
    isEqual = "É igual"
    if s == 0 :
        e = len(word1)-1

    if s == len(word1):
        return isEqual
    firstChar = word1[s]
    lastChar = word1[e]

    if firstChar != lastChar:
        isEqual = "Não é igual"
        return isEqual
    return verificarPalindromo(word1, e-1, s+1)

print(verificarPalindromo('arara'))