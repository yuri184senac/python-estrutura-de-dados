class Automovel:
    placa = None;
    def __init__(self):
        self = None;
    
    def set_placa(self):
        self.placa = '123';
    
    def get_placa(self):
        return self.placa;
    
    def dirigir(self, velocidade): 
        print(f'Estou dirigindo {velocidade} km/h');
        
    def __str__(self) -> str: #Isso aqui é uma msg default da classe.
        return f'testando';


    
    
        