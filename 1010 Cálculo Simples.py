cod,quantidade,valor = input().split()
cod = int(cod)
quantidade = int(quantidade)
valor = float(valor)

cod2,quantidade2,valor2 = input().split()
cod2 = int(cod2)
quantidade2 = int(quantidade2)
valor2 = float(valor2)

subtotal = valor*quantidade
subtotal2 = valor2*quantidade2
total = subtotal+subtotal2

print(f"VALOR A PAGAR: R$ {total:.2f}")

# class Carro:
    
    
#     def andar(self):
#         print("Andando")
        
# celta = Carro()
# celta.andar()

# nicolas="O nicolas é um programador"
# for palavra in nicolas.split(" "):
#     print(palavra)