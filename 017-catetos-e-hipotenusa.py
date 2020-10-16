#   faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot

catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
#hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")
