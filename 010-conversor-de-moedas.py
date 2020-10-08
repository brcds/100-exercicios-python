# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# Dólar ela pode comprar.
# considere US$1.00 = R$3.27

dinheiro = float(input('Quanto de dinheiro você tem na carteira? '))

print(f'\nCom R${dinheiro} você pode comprar US${dinheiro / 3.27} Dólares!')