d = int(input())
dia = (d % 365) % 30
mes = (d % 365) // 30
ano = d // 365

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")



