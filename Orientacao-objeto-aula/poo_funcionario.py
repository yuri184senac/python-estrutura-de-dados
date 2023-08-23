class funcionario:
    def __init__(self):
        self.__salario = None; #atributo privado
        self.__nome = None;
        
    def getNome(self):
        return self.__nome;
    
    def setNome(self, nome):
        self.__nome = nome;
        
    def getSalario(self):
        return self.__salario;
    
    def setSalario(self, salario):
        self.setSalario = salario;
    
yuri = funcionario();
yuri.__nome ='rr'
yuri.setNome('Yuri Conder')
print(yuri.getNome());