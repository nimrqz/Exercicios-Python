sal = float(input())

if sal > 0 and sal <= 400.00:
    novosal = sal + (sal*0.15)
    ganho = (novosal - sal)
    porcent = 15
if sal >= 400.01 and sal <= 800.00:
    novosal = sal + (sal*0.12)
    ganho = (novosal - sal)
    porcent = 12
if sal >= 800.01 and sal <= 1200.00:
    novosal = sal + (sal*0.10)
    ganho = (novosal - sal)
    porcent = 10
if sal >= 1200.01 and sal <= 2000.00:
    novosal = sal + (sal*0.07)
    ganho = (novosal - sal)
    porcent = 7
if sal > 2000.00:
    novosal = sal + (sal*0.04)
    ganho = (novosal - sal)
    porcent = 4
    
print(f"Novo salario: {novosal:.2f}")
print(f"Reajuste ganho: {ganho:.2f}")
print(f"Em percentual: {porcent:.0f} % ")