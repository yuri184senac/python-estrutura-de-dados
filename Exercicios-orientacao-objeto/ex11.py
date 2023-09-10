class Carro:
    def __init__(self, consumo, capacidadeCombustivel=0):
        self.consumo = consumo #km/l
        self.capacidadeCombustivel = capacidadeCombustivel

    def andar(self, dist):

        combustivel_gasto = dist/self.consumo
        self.capacidadeCombustivel -= combustivel_gasto
        print(f'Andou {dist} Km')

        
    def obterGasolina(self):
        print(f'Combustível atual:{self.capacidadeCombustivel} L')
        return self.capacidadeCombustivel
    
    def adicionarGasolina(self, qtde):
        print(f'Foi abastecido:{qtde} L')
        self.capacidadeCombustivel += qtde
    
meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(20)
meuFusca.obterGasolina()

