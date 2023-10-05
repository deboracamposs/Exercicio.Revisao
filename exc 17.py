#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia
#o número de maçãs compradas, calcule e escreva o custo total da compra.
print('--- PREÇO DAS MAÇÃES --- \n Unidade a R$1,30 \n Unidade em dúzia a R$1,00')
nmacas = float(input('Digite o número de maçãs: ' ))
precomaca = 1.0
if nmacas < 12:  # Se comprar pelo menos uma dúzia
    precomaca = 1.3
else:
    precomaca = 1.0
custo = nmacas * precomaca
print(f'O custo das maçãs é: R${custo:.2f}')