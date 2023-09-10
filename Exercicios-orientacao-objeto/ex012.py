class ContaBancaria:
    
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero;
        self.nome = nome;
        self._saldo = saldo;

    def alterarNome(self, nome):
        self.nome = nome;

    def depositar(self, valor):
        self._saldo = valor;

    def sacar(self, valor):
        self._saldo = valor;

    def get_saldo(self):
        return self._saldo;

    def __str__(self):
        return f'Nome:{self.nome} Conta:{self.numero} Saldo R${self.get_saldo()}'

class ContaInvestimento(ContaBancaria):
    def __init__(self, numero, nome, saldo, taxJuros):
        super().__init__(numero, nome, saldo)
        self.taxJuros = taxJuros

    def adicioneJuros(self, parcelas):
        juros= self._saldo * self.taxJuros/100 * parcelas 
        self._saldo += juros

conta1 = ContaInvestimento(12345678, 'Yuri Roliz', 1000, 10)
conta1.adicioneJuros(5)
print(conta1)