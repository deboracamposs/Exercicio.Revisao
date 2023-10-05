#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o
#percentual que cada um representa em relação ao total de eleitores.
total_eleitores = float(input("Digite o número total de eleitores: "))
votos_brancos = float(input("Digite o número de votos em branco: "))
votos_nulos = float(input("Digite o número de votos nulos: "))
votos_validos = float(input("Digite o número de votos válidos: "))

percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100


print("Percentual de votos em branco:", percentual_brancos, "%")
print("Percentual de votos nulos:", percentual_nulos, "%")
print("Percentual de votos válidos:", percentual_validos, "%")