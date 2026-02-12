n1, n2, n3, n4 = input().split()
n1 = int(float(n1)*10)
n2 = int(float(n2)*10)
n3 = int(float(n3)*10)
n4 = int(float(n4)*10)
media = ((n1*0.2)+(n2*0.3)+(n3*0.4)+(n4*0.1))/10
print(f"Media: {media:.1f}")
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    media2 = input()
    media2 = float(media2)
    print(f"Nota do exame: {media2:.1f}")
    
    media_final = (media + media2) / 2
    media_final = float(media_final)
    
    if media_final >= 5:
        print("Aluno Aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")