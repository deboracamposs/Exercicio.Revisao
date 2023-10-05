#Escreva um algoritmo para ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente
n1=int(input('Digite o número:'))
n2=int(input('Digite o número:'))
while n1 == n2:
    print('O valores não podem ser iguais')
    n1 = int(input('Digite o número:'))
    n2 = int(input('Digite o número:'))
if n1 > n2:
    print(f'A sequência crescente: {n2} , {n1}')
else:
    print(f'A sequência crescente: {n1}, {n2}')