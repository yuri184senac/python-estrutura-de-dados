animals = ['gato', 'tatu', 'rato', 'pato'];

print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])
print('#-------------------------------------------')
notas = [0, 10.0, 7.0, 7.0, 8.0, 8.0]
notas.insert(1, 500)
print(notas)

#remover:
notas.remove(0)
print(notas)

print('#-------------------------------------------')
notas.sort() #Ordena do menor para o maior
print(notas)

print(sorted(animals)) #Só altera o output.
print(animals)

print('#-------------------------------------------')
notas.extend(animals)
print(notas)
print('#-------------------------------------------')
#Operacoes matematicas com listas
exemplo = ['z', 'y'] + ['x',]

print(exemplo)

exemplo +=[3,]
print(exemplo)
exemplo *=2;
print(exemplo)

