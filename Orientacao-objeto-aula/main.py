import poo_automovel
if __name__ == '__main__':
    corola = poo_automovel.Automovel();
    fusca = poo_automovel.Automovel();
    
    fusca.set_placa()
    print(corola.get_placa());
    print(fusca.get_placa());