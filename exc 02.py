#CRIAR UM CÓDIGO QUE LEIA UM NÚMERO DIFERENTE DE ZERO E DIGA SE ESTE NÚMERO É POSITIVO OU NEGATIVO
n=int(input('Digite o número:'))
while n == 0:
    n=int(input('Número inválido.Digite novamente o número:'))

if n > 0:
  print(f'Este número {n} é positivo')
else:
  print(f'Este número {n} é negativo')
print('Programa finalizado!')