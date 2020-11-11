'''
    Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = str(input('Qual seu nome completo? '))

existeSilva = 'SILVA' in nome.upper()
print(f'Seu nome tem "SILVA"? {existeSilva}')
