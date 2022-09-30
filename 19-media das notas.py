'''
Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua 
média e mostre na tela. No final, analise a média e mostre se o aluno teve 
ou não um bom aproveitamento (se ficou acima da média 7.0).
'''

pergunta = input('Qual é seu nome?: ')

nota1 = float(input('Qual é sua primeira nota?: '))
nota2 = float(input('Qual é sua segunda nota?: '))

calculo = (nota1 + nota2) / 2

if calculo >= 7:
    print('Aluno(a):{} sua media é {} continue assim.'.format(pergunta,calculo))

else:
    print('Aluno(a):{} sua media é {} estude mais!'.format(pergunta,calculo))