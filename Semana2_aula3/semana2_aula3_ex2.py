'''Ex 02 aula 3'''

meses_do_ano = (
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro")

x = int(input("Digita ai o numero do mês do ano que deseja:"))
print(f"O mês que vocês esta falando é o {meses_do_ano[x-1]}")