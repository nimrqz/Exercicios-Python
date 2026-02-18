

def ler_valores[T](type:T)->tuple[T,T,T,T]:
    valores = input().split()
    for i in range(0,len(valores)):
        valores[i] = type(valores[i])
    return tuple(valores)

def solucao():
    a,b,c,d, = ler_valores(int)
    

    if b > c and d > a and c+d > a+b and c>0 and d>0 and a % 2 == 0:
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")
        
    
def teste():
    a,b,c,d,*resto = ler_valores(int)
    print(type(a))
    

def main():
    solucao()
    # teste()

    
    
if __name__ == "__main__":
    main()