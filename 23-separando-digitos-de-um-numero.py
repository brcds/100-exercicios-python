'''
    faça um programa que leia uma número de 0 a 9999 e mostre na tela cada um
    dos digitos separados.
ex:
    Digite um número: 1834
    unidade: 4 dezena: 3 centena: 8 milhar: 1
'''

numero = int(input('Informe um numero: '))

print(f'Analisando o numero {numero}\n'
      f'Unidade: {numero // 1 % 10}\n'
      f'Dezena: {numero // 10 % 10}\n'
      f'Centena: {numero // 100 % 10}\n'
      f'Milhar: {numero // 1000 % 10}')

