# faça um programa que receba um salario e calcule 15% de sobre o valor;

salario = float(input('Informe seu salario para receber um aumento: '))

print(f'O seu salario era R${salario:.2f}, com o aumento de 15% '
      f'você vai receber R${salario + (salario * 15 / 100):.2f}')
