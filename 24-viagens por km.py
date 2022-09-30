'''
Faça um algoritmo que pergunte a distância que um passageiro deseja 
percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para 
viagens até 200Km e R$0.45 para viagens mais longas. 
'''

print('A passagem ta 0,50 centavos por KM, acima de 200km você pagara 0.45 centavos')
print('Por quantos KM você deseja vijar?')
pergunta = int(input('Digite aqui: '))

mult = pergunta * 0.50
mult1 = pergunta * 0.45

if pergunta <= 200:
    print('O preço da passagem é de R${:.2f}'.format(mult))
else:
    print('O preço da passagem é de R${:.2f}'.format(mult1))