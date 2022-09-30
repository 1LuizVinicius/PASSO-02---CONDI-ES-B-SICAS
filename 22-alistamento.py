'''
Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua 
situação em relação ao alistamento militar. 

- Se estiver antes dos 18 anos, mostre em quantos anos faltam para o 
alistamento. 
- Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do 
alistamento. 
'''

print("Você quer saber se pode ou não se alistar no exercito?")
pergunta = int(input('Digite o ano que você nasceu: '))

dim = 2022 - pergunta
ano =  dim  - 18
ano1 = 18 - dim

print("Você tem",dim)

if dim >= 18:
    print("Com",dim,"ja pode se alistar no exercito")
    print('Você passou',ano,'ano(s) do do seu alistamento')
else:
    print('Com',dim,"ainda não pode se alistar no exercito!")
    print('ainda faltam',ano1,'ano(s) para se alistar')