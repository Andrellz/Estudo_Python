'''EX 02'''


notas_str = input("Digitar notas: ")

lista_notas_str = notas_str.split(',')

lista_notas_float = [float(nota) for nota in lista_notas_str]

soma_notas = sum(lista_notas_float)

media = soma_notas / len(lista_notas_float)

print(f"A média das notas é: {media:.2f}")

if media > 6.0:
    print("Situação: Aprovado!")
elif media >= 4.0:
    print("Situação: Recuperação.")
else:
    print("Situação: Reprovado.")