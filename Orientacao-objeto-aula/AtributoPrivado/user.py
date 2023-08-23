class User:
    def __init__(self, name):
        self.__name = name;

    def get_name(self):
        return self.__name

    def set_name(self, newName):
        self.__name = newName


p1 = User('Yuri');

p1.__name = 'bruna2'

print(p1.get_name())
