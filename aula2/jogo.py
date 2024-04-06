nome_time1 = input("Informe o nome do time: ")
gols_time1 = input(f'Informe o número de gols do time {nome_time1}: ')
nome_time2 = input("Informe o nome do outro time: ")
gols_time2 = input(f'Informe o número de gols do time {nome_time2}: ')
if gols_time1 == gols_time2:
    print("Empate")
if gols_time1 > gols_time2:
    print(f'O time vencedor foi: {nome_time1}')
else:
    print(f'O time vencedor foi: {nome_time2}')