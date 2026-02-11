x1, y1 = input().split()
x2, y2 = input().split()
y1 = float(y1)
y2 = float(y2)
x1 = float(x1)
x2 = float(x2)

distancia = ((x2-x1)**2+(y2-y1)**2)**0.5

print(f"{distancia:.4f}")