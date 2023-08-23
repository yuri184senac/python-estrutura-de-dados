class Student:

    def __init__(self, name):
        self._name = name;


    @property
    def name(self):
        return self._name;

    @name.setter
    def name(self, newName):
        self._name = newName;

    @name.getter
    def name(self):
        print('getter method was called');
        return self._name;

std = Student('bruna');


print(std.name)






