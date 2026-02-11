n = float(input())
n = int(n*100)
print("NOTAS:")

for dinheiro in [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]:
    quantidade = n // dinheiro
    n = n % dinheiro
    mostrar = dinheiro/100.0
    if mostrar == 1:
        print(f"MOEDAS:")
    if mostrar <= 1:
        print(f"{quantidade:.0f} moeda(s) de R$  {mostrar:.2f}")
    elif mostrar >= 1:
        print(f"{quantidade:.0f} nota(s) de R$  {mostrar:.2f}")