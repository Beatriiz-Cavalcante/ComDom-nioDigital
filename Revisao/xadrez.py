'''Escreva um algoritmo para ler a hora de início e a hora de fim de um jogo de xadrez (considere apenas horas inteiras,
sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas
e que o jogo pode iniciar em um dia e terminar no dia seguinte'''

horaInicio = int(input("Digite a hora de início da partida: "))
horaFim = int(input("Digite a hora de término da partida: "))


if horaInicio > horaFim:
    duracao = horaInicio - horaFim
    print(duracao)
else:
    duracao = horaFim - horaInicio
    print(duracao)