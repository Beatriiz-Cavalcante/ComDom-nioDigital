entrada01 = "3:45"
entrada02 = "14:20"

horas01, minutos01 = map(int, entrada01.split(':'))
horas02, minutos02 = map(int, entrada02.split(':'))

total_minutos = (horas01 * 60 + minutos01) + (horas02 * 60 + minutos02)

horas_saida = total_minutos // 60 #//para pegar só a parte inteira (esse resultado considerando o modelo 24h)
horas_saida = horas_saida - 12 #(esse resultado considerando o modelo 12h)
minutos_saida = total_minutos % 60


print("Saída:", f"{horas_saida}:{minutos_saida:02d}")