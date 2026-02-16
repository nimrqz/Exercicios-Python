<<<<<<< HEAD
positivos = 0
negativos = 0
pares = 0
impar = 0

for i in range(5):
    valor = float(input())
    
    if valor > 0:
        positivos += 1
    if valor < 0:
        negativos += 1
    if valor % 2 == 0:
        pares += 1
    if valor % 2 == 1:
        impar += 1

print(f"{pares} valor(es) pares(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
=======
positivos = 0
negativos = 0
pares = 0
impar = 0

for i in range(5):
    valor = float(input())
    
    if valor > 0:
        positivos += 1
    if valor < 0:
        negativos += 1
    if valor % 2 == 0:
        pares += 1
    if valor % 2 == 1:
        impar += 1

print(f"{pares} valor(es) pares(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
>>>>>>> 322bd096308664fac43211a0c0fa41c63f422951
