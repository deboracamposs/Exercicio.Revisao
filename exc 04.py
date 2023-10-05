#CRIE UM ALGORITMO QUE RECEBA 3 NÚMEROS E INFORME QUAL O MAIOR ENTRE ELES
n1=int(input('Digite o número 1:'))
n2=int(input('Digite o número 2:'))
n3=int(input('Digite o número 3:'))
if n1 > n2 and n1 > n3:
    print(f'O número maior é: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O número maior é: {n2}')
else:
    print(f'O número maior é: {n3}')