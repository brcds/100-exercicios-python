'''
crie um programa que leia o nome completo de uma pessoa e mostre.
o nome com todas as letras maiusculas e minusculas.
quantas letras ao todo(sem considerar espaços)
quantas letras tem o primeiro nome '''

nome = input("Digite seu nome: ").strip() #remove espaços antes e depois.

print(f'\n'
      f'Seu nome em letras maiusculas: {nome.upper()}\n'
      f'Seu nome em letras minusculas: {nome.lower()}\n'
      f'Total de letras no seu nome: {len(nome) - nome.count(" ")}\n'
      # f'Numero de letras do seu primeiro nome: {nome.find(" ")}'
      f'\n')

