# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um número: '))

print(f'O dobro de {numero} é {numero * 2}.\n'
      f'O triplo de {numero} é {numero * 3}.\n'
      f'A raiz quadrada de {numero} é {numero ** (1/2):.2f}.')