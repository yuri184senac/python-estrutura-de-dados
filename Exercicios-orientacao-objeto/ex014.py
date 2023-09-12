# Yuri Conder Roliz Sabbagh
class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self.__salario = salario
    
    @property
    def nome(self):
        return self._nome
    
    @nome.getter
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self.__salario
    
    @salario.getter
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novoSalario):
        self.__salario = novoSalario
    
    def aumentarSalario(self, percentualAumento):
        self.__salario += self.__salario * percentualAumento/100 
    
p1 = Funcionario('Yuri', 1000)
p1.__salario = 200 #Professor, repare que não conseguimos alterar o valor do salário diretamente
print('Nome:', p1.nome)
print('Salario:', p1.salario)

p1.aumentarSalario(10)
print('Salario:', p1.salario)

