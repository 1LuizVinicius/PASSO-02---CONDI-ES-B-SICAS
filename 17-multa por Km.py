'''
Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 
80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba 
o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
'''

print('Você recebera uma multa de R$5 por cada km acima de 80')
pergunta = float(input('Qauntos KM/H você estava?: '))

calculando = (pergunta - 80) * 5

if pergunta <= 80:
    print('Muito bem, continue assim.')

else:
    print('Você receberaa uma multa de R${}.'.format(calculando)) 