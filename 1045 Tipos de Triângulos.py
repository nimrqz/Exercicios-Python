a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
maior = a
meio = b
menor = c

if a > b and a > c:
    maior = a
    if b > c:
        meio = b
        menor = c
    else:
        meio = c
        menor = b
    
elif b > a and b > c:
    maior = b
    if a > c:
        meio = a
        menor = c
    else:
        meio = c
        menor = a
elif c > a and c > b:
    maior = c
    if a > b:
        meio = a
        menor = b
    else:
        meio = b
        menor = a

if maior >= meio+menor:
    print("NAO FORMA TRIANGULO")
    exit()
if maior**2==(meio**2)+(menor**2):
    print("TRIANGULO RETANGULO")
if maior**2> ((meio**2) + (menor**2)):
    print("TRIANGULO OBTUSANGULO")
if maior**2<(meio**2)+(menor**2):
    print("TRIANGULO ACUTANGULO")
if maior == meio and meio == menor:
    print("TRIANGULO EQUILATERO")
if (maior == meio and maior != menor) or (menor == meio and menor != maior) or (maior == menor and maior != meio):
    print("TRIANGULO ISOSCELES")