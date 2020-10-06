# Faça um programa que leia um numero inteiro e em seguida mostre sua tabuada.

numero = int(input('Digite um número para ver sua tabuada: '))

print('-' * 10)

for c in range(1, 11):
    print(f'{numero} * {c} = {numero * c}')

print('-' * 10)

