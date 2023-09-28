#Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci.
# Alguns números desta sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(50))
   
   
