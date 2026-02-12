a, b, c= input().split()
a = float(a)
b = float(b)
c = float(c)

if a + b > c and b + c > a and c + a > b:
    resultado1 = a+b+c
    print(f"Perimetro = {resultado1:.1f}")
else:
    resultado2 = (((a+b)*c)/2)
    print(f"Area = {resultado2:.1f}")