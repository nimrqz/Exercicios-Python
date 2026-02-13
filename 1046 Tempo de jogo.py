a, b = input().split()
a = int(a)
b = int(b)

if b > a:
    horas = b - a
else:
    horas = (24 - a) + b

print(f"O JOGO DUROU {horas} HORA(S)")