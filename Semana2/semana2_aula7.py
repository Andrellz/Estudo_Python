"""
I/O Input and Output
"""

print('hello world', 'Maria', 1, True)
print('hello world', 'Maria', 1, True, sep='@')
print('hello world', 'Maria', 1, True, sep='@', end='!!!\n')

arquivo = open('nomes.txt', 'w', encoding='utf-8')
print('joao@email.com', 'maria@email.com', 'pedro@email.com', file=arquivo)
print('joao@email.com', 'maria@email.com', 'pedro@email.com', file=arquivo, sep=';')

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
print(type(nome), type(idade))

# idade = int(input('Digite sua idade: '))

if idade >= 18:
    print(f'{nome}, você é maior de idade')
else:
    print(f'{nome}, você é menor de idade')

arquivo_notas = open('notas.txt', 'r', encoding='utf-8')
conteudo = arquivo_notas.read()
print(conteudo)
print(conteudo.split(sep=';'))

notas = conteudo.split(sep=';')
print(notas)
notas = [float(nota) for nota in notas]
print(notas)
media = (notas + notas + notas) / len(notas)
print(media)