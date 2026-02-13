sal = float(input())

if sal >= 0 and sal <= 2000.00:
    print("Isento")
    exit()
    
if sal >= 2000.01 and sal <= 3000.00:
    salisento = sal - 2000
    salnovo = (salisento*0.08)
    print(f"R$ {salnovo:.2f}")
    
if sal >= 3000.01 and sal <= 4500.00:
    salisento = sal - 2000
    salbaixo = (salisento - 1000)
    salmedio = ((salbaixo*0.18) + (salisento*0.08))
    print(f"R$ {salmedio}")