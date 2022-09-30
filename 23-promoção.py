'''
 Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos 
para todos, mas especialmente para mulheres. Faça um programa que leia nome, 
sexo e o valor das compras do cliente e calcule o preço com desconto. 
Sabendo que: 

- Homens ganham 5% de desconto 
- Mulheres ganham 13% de desconto 
'''

pergunta = input('Qual seu nome?: ')
print('responda com f(feminino) ou m(masculino)')
pergunta1 = input('Qual seu sexo?: ')

compra = float(input('Dgite o valor da compra: '))

homens = compra - (compra * 5/100)
mulheres = compra - (compra * 13/100)

if pergunta1 =='f':
    print('Total de {:.2f} com 13% de desconto.'.format(mulheres))
else:
    print('Total de {:.2f} com 5% de desconto.'.format(homens))