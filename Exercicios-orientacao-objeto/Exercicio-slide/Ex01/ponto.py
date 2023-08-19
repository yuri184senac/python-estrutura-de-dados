class Ponto:
    def __init__(self,nome, x, y):
        self.nome = nome;
        self.x = x;
        self.y = y;

    def __str__(self):
        return print(f'Nome:{self.nome}: x:{self.x} y:{self.y}');

