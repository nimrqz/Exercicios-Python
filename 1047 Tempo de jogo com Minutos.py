a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

inicio = a * 60 + b
fim = c * 60 + d

total = fim - inicio

if total <0:
    total += 24*60

h = total // 60
m = total % 60
     
print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")