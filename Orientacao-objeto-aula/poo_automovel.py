class Automovel:
    
    def __init__(self, placa):
        self.set_placa(placa);
    
    def set_placa(self, placa):
        self.placa = placa;
        
    
    def get_placa(self):
        return self.placa;
    
    def dirigir(self, velocidade): 
        print(f'Estou dirigindo {velocidade} km/h');
        
    def __str__(self) -> str: #Isso aqui é uma msg default da classe.
        return f'testando';


    
fusca = Automovel('1213')

print(fusca.__str__())


        