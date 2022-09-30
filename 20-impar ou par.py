'''
Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou 
ÍMPAR.
'''
print('Você quer saber se o número e per ou impar?')
pergunta = int(input('Digite uma número: '))

resultado = pergunta % 2

print('Você digitou o número',pergunta)

if resultado == 1: 
    print(pergunta,'é ímpar')

else:
    print(pergunta,'é par')