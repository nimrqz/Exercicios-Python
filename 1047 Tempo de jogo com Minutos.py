a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if c > a:
    horas = c - a
else:
    horas = (24 - a) + c
    
if d > b:
    minutos = d - b
else:
    minutos = (60 - b) + c
if minutos == 60:
    minutos = 0

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTOS(S)")