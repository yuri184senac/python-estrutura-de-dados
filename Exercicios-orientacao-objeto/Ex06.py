# Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class Televisao:

    def __init__(self, volume=0, canal=0):
        self._volume = volume;
        self._canal = canal;

    @property
    def volume(self):
        return self._volume;

    @volume.setter
    def volume(self, value):
        if not((value > 0 ) and (value < 100)) :
            raise 'Volume fora da faixa do limite'
        self._volume = value;

    @property
    def canal(self):
        return self._canal;

    @canal.setter
    def canal(self, value):
        if (value < 0):
            raise 'Não existem canais abaixo do número 0'
        print('Você mudou o canal para', value);
        self._canal = value;


lg = Televisao()
lg.canal = 10;
lg.volume = 14
print(f'Audio: {lg.volume}');
print(f'Canal: {lg.canal}');






