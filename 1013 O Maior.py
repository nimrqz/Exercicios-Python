a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

abs1 = abs(a-b)
formula1 = (((a+b)+abs1)/2)

abs2 = abs(formula1-c)
formuala2 = (((formula1+c)+abs2)/2)

print(f"{formuala2:.0f} eh o maior")