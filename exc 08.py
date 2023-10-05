#FAÇA UM CÓDIGO QUE RECEBA 4 NÚMEROS E REALIZE A SOMA DELES E A MÉDIA ENTRE ELES. E MOSTRE OS RESULTADOS
soma = 0
x = 0
for x in range(4):
    numero=int(input('Digite o número:'))
    soma = numero+soma
media=soma/4
print(f'A soma é {soma} e a média é {media}')