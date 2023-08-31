class ContaCorrente:
    
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

usr = ContaCorrente('123', 'yuri');

print(usr)

usr.depositar(20);

print(f'Novo saldo da conta R${usr.get_saldo()}')


        


            