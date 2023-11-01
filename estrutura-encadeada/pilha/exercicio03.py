#3. Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais. Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.

class Nodo:
    """Esta classe representa um nodo de uma estrutura."""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior
        
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

class Pilha:
  def __init__(self):
     self.topo = None
     self.count = 0 
  def insere(self, novo_dado):
        #Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)
        
        # Faz com que o novo nodo seja o topo da pilha
        novo_nodo.anterior = self.topo
        
        #Faz com que a cabeça da lista referencia o novo nodo.
        self.topo = novo_nodo
        self.count+=1
        pass
    
  
  def remove(self):
        assert self.topo, "Impossível remover o valor da pilha"       
        pop = self.topo.dado
        self.topo = self.topo.anterior
        return pop

  def __repr__(self):
       return "[" + str(self.topo) + "]"
  

listaPilha1 = [1,2,3,4,5,8]
listaPilha2 = [1,2,3,4,5,8]

p1 = Pilha()
p2 = Pilha()

for i in range(len(listaPilha1)):
    p1.insere(listaPilha1[i])

for i in range(len(listaPilha2)):
    p2.insere(listaPilha2[i])

def compararPilhas(pilha1, pilha2):
      p1_len = pilha1.count
      p2_len = pilha2.count
      resultado = 'São iguais'
      if not p1_len == p2_len:
        resultado = 'Não são iguais'
        print('fodase')
        
      tamanho = p1_len
      for i in range(tamanho):
        elemento_p1 = pilha1.remove()
        elemento_p2 = pilha2.remove()
        if (elemento_p1 != elemento_p2):
          resultado = 'Não são iguais'
          return resultado       
      return resultado
x = compararPilhas(p1, p2)
print(x)
