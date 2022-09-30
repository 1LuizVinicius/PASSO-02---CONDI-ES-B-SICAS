'''
Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade 
dela e depois mostre se ela pode ou não votar. 
'''

pergunta = int(input('Qual é sua idade?: '))

if pergunta >=18:
    print('Você ja pode votar')
else:
    print('Você ainda nao pode votar!')