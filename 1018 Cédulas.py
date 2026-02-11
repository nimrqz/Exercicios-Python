n = int(input())

for cedula in [100, 50, 20, 10, 5, 2, 1]:
    quantidade = n // cedula
    print(f"{quantidade} nota(s) de R$ {cedula},00")
    n = n % cedula