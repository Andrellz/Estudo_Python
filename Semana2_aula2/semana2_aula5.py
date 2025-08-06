'''Tipos de dados'''

# Tipos Numéricos
idade = 30
peso = 75.5

# Strings
nome = "João"
sobrenome = "Silva"
nome_completo = f"Olá, {nome} {sobrenome}"
print(nome_completo)
print(nome[0])
print(nome[-1])
print(nome_completo.lower())
print(nome_completo.upper())

# Booleanos
ligado = True
resultado = 10 == 10

# Listas
frutas = ["maçã", "banana", "uva"]
print(frutas[0])
frutas[0] = "abacaxi"
frutas.append("morango")
print(len(frutas))
for fruta in frutas:
    print(fruta)

# Tuplas
codigos = (10, 20, 30)
print(codigos[0])

# Conjuntos (Sets)
resultado_sorteio = {10, 5, 2, 8, 10}
resultado_sorteio.add(7)

# Dicionários
funcionario = {
    "nome": "Maria",
    "idade": 28,
    "cargo": "Gerente"
}
print(funcionario["nome"])
print(funcionario.keys())
print(funcionario.values())
funcionario["idade"] = 29