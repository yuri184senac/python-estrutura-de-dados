from fila import Fila, FilaService



f1 = Fila()
f1.inserir(1)
f1.inserir(2)
f1.inserir(3)
f1.inserir(3)
f1.inserir(4)
f1.inserir(5)
f1.inserir(6)
f1.inserir(7)
f1.inserir(8)
f1.inserir(9)
f1.inserir(9)
f1.inserir(9)
f1.inserir(9)
f1.inserir(10)
f1.inserir(11)
f1.inserir(12)

print(f1)
FilaService.recoverElemento(f1, 3)
print('APOS REMOÇÃO')
print(f1)





