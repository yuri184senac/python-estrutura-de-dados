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
  def recoverElemento(fila: Fila, target):
    recover = None;
    count = 0; #Esse count foi criado para auxiliar no backup da fila original
    fila_fantasma = Fila();
    try: 
      element= ''
      while element != None: #Contando o numero de elementos na fila utilizando essa condição
        element = fila.remove()
        if element == target and recover!=target: #Remove o elemento alvo da fila e verifica se esse elemento já foi removido antes
          recover = element;
        else:
          fila_fantasma.inserir(element)
          count +=1
    except: #Tratamento de erro para quando o alvo procurado dentro da fila não existir
      if (target == recover):
        pass
      else:
        print('Não achamos o elemento procurado')  
  
    print('ANTES - FILA FANTASMA',fila_fantasma)
    #Nessa parte do código faço a inserção da fila fantasma na fila original
    i = 0;
    while i <= count-1:
       x = fila_fantasma.remove()
       fila.inserir(x)
       i+=1
    print('ELEMENTO RECUPERADO',recover)
    print('DEPOIS - FILA FANTASMA',fila_fantasma)
    return recover




