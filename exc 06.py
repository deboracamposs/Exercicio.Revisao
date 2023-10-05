#LER UM VALOR E ESCREVER A MENSAGEM É MAIOR QUE 10! SE O VALOR LIDO FOR MAIOR QUE 10, CASO CONTRÁRIO ESCREVER NÃO É MAIOR QUE 10!
n=int(input('Digite um número:'))
if n > 10:
    print(f'O número {n} é MAIOR do que 10')
elif n < 10:
    print(f'O número {n} é MENOR do que 10')
else:
    print('Programa Finalizado')