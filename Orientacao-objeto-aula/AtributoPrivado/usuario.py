class Usuario:
    
   
    @property
    def idade(self):
        print('Getter method called');
        return self.age;
    
    @idade.setter
    def idade(self, a):
        if (a < 18):
            raise ValueError('Idade menor do que 18');
        print('setter method called');
        self.idade = a;



usr =  Usuario();
usr.idade = 19;
print(usr.idade);
usr.idade = 20;
print(usr.idade);


