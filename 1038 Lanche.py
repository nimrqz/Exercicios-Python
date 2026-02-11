i1, i2 = input().split()

i1 = int(i1)
i2 = int(i2)

id = [4.00, 4.50, 5.00, 2.00, 1.50]

print(f"Total: R$ {id[i1-1]*i2:.2f}")