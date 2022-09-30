'''
Faça um algoritmo que leia um determinado ano e mostre se ele é ou não 
BISSEXTO.
'''

pergunta = int(input("Digite um ano: "))

if pergunta % 100 != 0 and pergunta % 4 == 0 or pergunta % 400 == 0:
    print(pergunta,"é um ano bissexto")

else:
    print(pergunta,"nao é bissexto")