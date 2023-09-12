# Yuri Conder Roliz Sabbagh

class Ponto:

  def __init__(self, x,y):
    self.x = x;
    self.y = y;

  def get_valorX(self):
    return self.x;

  def get_valorY(self):
    return self.y

class Retangulo():
  
  def __init__(self, largura, altura):
    self.largura = largura
    self.altura = altura

  def get_centro(self):
    return f'x:{self.largura/2}, y:{self.altura/2}'
    
  
vert1 = Ponto(0,0)
vert2 = Ponto(0,6)
vert3 = Ponto(8,6)
vert4 = Ponto(8,0)

altura = vert2.get_valorY() - vert1.get_valorY()
largura = vert4.get_valorX() - vert1.get_valorX()

retangulo1 = Retangulo(largura, altura)

print(retangulo1.get_centro())

  