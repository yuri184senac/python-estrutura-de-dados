class BombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, qtde_combustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self._qtde_combustivel = qtde_combustivel

    def abastecerPorValor(self, valor):
         total_litros = valor / self.valorLitro
         self.alterarQtdeCombustivel(total_litros)
         return f'Foram colocados {total_litros} de {self.tipoCombustivel} no seu veículo'
    
    def abastecerPorLitro(self, qtde):
         preco =  qtde * self.valorLitro
         self.alterarQtdeCombustivel(qtde)
         return f'Valor a pagar R${preco}'
    
    def altetarValor(self, novoValor):
        self.valorLitro = novoValor

    def alterarCombustivel(self, tipo):
        self.tipoCombustivel = tipo

    def alterarQtdeCombustivel(self, qtde):
        print('Quantidade de combustível disponível:', self._qtde_combustivel)
        if self._qtde_combustivel > qtde:
            self._qtde_combustivel -= qtde
            print('Quantidade de combustível após abastecimento', self._qtde_combustivel)
        else:
            print(f'Não há combustível suficiente na bomba')


carro1 = BombaCombustivel('gasolina', 2, 1000)
carro1.abastecerPorLitro(100)
print(carro1.abastecerPorValor(100))

carro1.alterarCombustivel('diesel')
carro1.altetarValor(1)
print(carro1.abastecerPorValor(10))