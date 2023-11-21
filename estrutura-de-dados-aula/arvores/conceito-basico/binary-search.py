list = [1,5,200,13,63,6,40,90]


def find(number, array) :
  for i in array:
    if (number == i) :
     return number;
  return False;
    
x = find(5, list);

if (x != False) :
  print('Achamos o número', x);
else:
  print('Não achamos o número')



   