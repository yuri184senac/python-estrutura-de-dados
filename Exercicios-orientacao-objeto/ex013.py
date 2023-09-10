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

    
p1 = Funcionario('Yuri', 1000)
p1.__salario = 200 #Professor, repare que não conseguimos alterar o valor do salário diretamente
print('Nome:', p1.nome)
print('Salario:', p1.salario)
