import os
iniciaScript = True;
inicializador = True
tocarMusica = False
NAME = 'D:'

while iniciaScript == True:
    inicializador = True;
    while inicializador==True:
        if (os.path.exists(('D:')) or os.path.exists(('E:')) or os.path.exists(('F:'))):
            inicializador = True;
            tocarMusica = True;
            print('PEN DRIVER CONECTADO');
            os.system('shutdown -a')
        else:
            if(tocarMusica):
                os.system('start C:/Users/36129382023.1n\Documents/roleta-russa/sound1.mp3');
            tocarMusica = False;
            print('PEN DRIVER REMOVIDO');
            break;