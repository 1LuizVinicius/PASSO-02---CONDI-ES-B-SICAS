'''
Crie um programa que leia o tamanho de três segmentos de reta. 
Analise seus comprimentos e diga se é possível formar um triângulo com essas 
retas. Matematicamente, para três segmentos formarem um triângulo, o 
comprimento de cada lado deve ser menor que a soma dos outros dois. 
'''

print('Imforme os lados A,B e C.')
a = int(input('Digite o lado A: '))
b = int(input('Digite o lado B: '))
c = int(input('Digite o lado C: '))

if ((a < (b+c)) and (b < (a+c)) and (c < (a+b))):
    print("É um triangulo")
else:
    print("Não é possivel formar um triangulo")