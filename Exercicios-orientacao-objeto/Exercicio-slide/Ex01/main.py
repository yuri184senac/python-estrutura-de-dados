from ponto import Ponto

arquivo = open('Exercicios-orientacao-objeto\Exercicio-slide\Ex01\pontos.txt');
def criarObjetoPonto():
    pontos = [];
    for line in arquivo:
        nome = line[0];
        x = line[1];
        y = line[2];
        ponto = Ponto(nome, x, y)
        pontos.append(ponto);
    return pontos
def mostrarPonto():
    pontos_array = criarObjetoPonto();
    for ponto in pontos_array:
          print(ponto.__str__());

mostrarPonto();


















