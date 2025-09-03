'''Ex 03 - Semana 2'''



intervalo_numerico = range(1,10)
lista_intervalo_numerido = list(intervalo_numerico)

numero_indificacao = "BR0j01X"



try:

    if numero_indificacao[0:2] == "BR" and numero_indificacao[6]== 'X' and int(numero_indificacao[2:6]) in lista_intervalo_numerido:
        print('ok, vamos seguir!')

    else:
        print("Esse número não está certo não caro colaborador, mais atenção por favor")

except ValueError:
    print("Esse número não está certo não caro colaborador, mais atenção por favor")

#if x = "BR" + lista_intervalo_numerido + "X"


