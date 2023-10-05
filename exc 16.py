#Escreva um algoritmo para ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule
#a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia
#seguinte
hora_inicio=int(input('Qual a hora do início?'))
hora_fim=int(input('Qual a hora do fim?'))
if hora_inicio >= hora_fim:
    duracao= (24 - hora_inicio) + hora_fim
else:
   duracao = 24 + (hora_fim - hora_inicio)
print(f'O tempo de partida foi: {duracao} horas')