'''
faça um programa que leia uma frase pelo teclado e mostre:
    > Quantas vezes aparece a letra A.
    > Em que posição ela aparece pela primeira vez.
    > Em que posição ela aparece pela última vez.
'''

Letra = 'A'

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count(Letra)}')
print(f'A primeira letra A apareceu na posição {frase.find(Letra)+1}')
print(f'A ultima letra A apareceu na posição {frase.rfind(Letra)+1}')

