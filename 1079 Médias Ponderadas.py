n = int(input())

for i in range(n):
    a, b, c = input().split()
    a = int(float(a)*10)
    b = int(float(b)*10)
    c = int(float(c)*10)
    resultado = (((a*0.2)+(b*0.3)+(c*0.5))/10)
    print(f"{resultado:.1f}")