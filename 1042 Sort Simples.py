n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor =n3
        meio = n2
    else:
        menor = n2
        meio = n3
if n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        menor =n3
        meio = n1
    else:
        menor = n1
        meio = n3
if n3 > n1 and n3 > n2:
    maior = n3
    if n1 > n2:
        menor =n2
        meio = n1
    else:
        menor = n1
        meio = n2
print(menor)
print(meio)
print(maior)
print()
print(n1)
print(n2)
print(n3)
        