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

<<<<<<< HEAD
if horas == 24 and minutos > 1:
    horas = 0
    
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTOS(S)")
=======

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTOS(S)")
>>>>>>> 8b197cc2d08ee1b219e1e0e740c5b6837265b537
