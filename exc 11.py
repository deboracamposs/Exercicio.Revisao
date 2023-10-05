#FAÇA UM ALGORITMO QUE LEIA A IDADE DE UMA PESSOA EXPRESSAS EM ANOS, MESES E DIAS E ESCREVA A IDADE
#DESSA PESSOA EXPRESSA EM DIAS. CONSIDERAR ANO COM 365 DIAS E MÊS COM 30
anos=int(input('Digite sua idade: '))
meses=int(input('Digite quantos meses tem: '))
dias=int(input('Digite os dias: '))
idadedias=anos*365+meses*30+dias

print(f'Você viveu {idadedias} dias')