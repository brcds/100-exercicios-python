#   faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import tan, cos, sin, radians

angulo = float(input("Digite um ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"o seno de {angulo} é {seno:.2f}\n"
      f"o cosseno de {angulo} é {cosseno:.2f}\n"
      f"a tangente de {angulo} é {tangente:.2f}")
      


