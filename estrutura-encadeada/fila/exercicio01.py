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
    self.primeiro = self.primeiro.proximo
    if self.primeiro == None:
      self.ultimo = None

  def __repr__(self) -> str:
    return "[" + str(self.primeiro) + "]"
  
