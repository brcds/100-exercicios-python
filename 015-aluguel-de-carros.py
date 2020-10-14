#   Escreva um programa que pergunte a quantidade km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado, calculo o preço a pagar. Sabendo que o
# carro custa R$60 por dia e R$0,15 por km rodado.

diasCarro = int(input("Quantos dias você passou com o carro: "))
kmRodado = float(input("Quantos km você rodou durante esse periodo: "))

print(f"você vai pagar um total de: {(diasCarro * 600) + (kmRodado * 0.15):.2f} pelo aluguel do carro! ")
