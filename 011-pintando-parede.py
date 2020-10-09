# 	faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e
# a quantidade de tinta necessaria para pintá-la. Sabendo que cada litro de tinta. Pinta uma area de 2m².

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2

print(
    f'Sua parede tem a dimensão de {largura}x{altura} e sua area é de {area}m²')

print(
    f'Para pintar essa parede você vai precisar de {tinta}l de tinta.')
