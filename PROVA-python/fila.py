class Nodo:
  def __init__(self, dado=0, proximo_nodo=None):
    self.dado = dado
    self.proximo = proximo_nodo

  def __repr__(self):
    return '%s -> %s' % (self.dado, self.proximo)

class Fila:
  """Representa uma fila usando estrutura encadeada"""

  def __init__(self):
    self.primeiro = None
    self.ultimo = None

  def inserir(self, novoDado):
    novo_nodo = Nodo(novoDado)

    if self.primeiro == None:
      self.primeiro = novo_nodo
      self.ultimo = novo_nodo
    else:
      self.ultimo.proximo = novo_nodo
      self.ultimo = novo_nodo

  def remove(self):
    """Remove o ultimo elemento da fila"""
    assert self.primeiro != None, "Impossivel remover elemento de uma fila vazia"        
    elementoRemovido = self.primeiro.dado
    self.primeiro = self.primeiro.proximo
    if self.primeiro == None:    
      self.ultimo = None
    return elementoRemovido

  def __repr__(self) -> str:
    return "[" + str(self.primeiro) + "]"


#LOGICA PARA RECUPERAR O ELEMENTO DA FILA
class FilaService:
  def recoverElemento( fila: Fila, target):
    recover = None;
    element = None;
    count = 0; #Esse count foi criado para auxiliar no backup da fila original
    
    try:
      travaRemocao = False; #Criamos essa flag para não remover todos os target da fila.
      fila_fantasma = Fila(); #Criamos um espelho da fila original
      while ((target != element)): #Condição para continuar buscando o alvo dentro fila 
        element = fila.remove()  # Armazenando o elemento removido da fila em uma variavel
        if ((target == element) and (not travaRemocao)): # Comparando se o elemento removido é igual ao que procuramos na fila
          recover = element; # Se for igual, vamos salvar esse elemento na variavável chamada recover
          element = None; # Aqui matamos a varíavel element
          travaRemocao = True;
        else:
         #Copiando elementos da fila original para a fila espelhada
          fila_fantasma.inserir(element)
        count +=1
    except: #Tratamento de erro para quando o alvo procurado dentro da fila não existir
      if (target == recover):
        pass
      else:
        print('Não achamos o elemento procurado')  
    for i in range(count-1):
      fila.inserir(fila_fantasma.remove())
    return recover
