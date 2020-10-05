# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

medida = float(input('Uma distância em metros: '))

print(f'A media de {medida}m corresponde a '
      f'{medida * 100:.0f}cm, '
      f'{medida * 1000:.0f}mm, '
      f'{medida * 10}dm, '
      f'{medida / 10}dam, '
      f'{medida / 100}hm e '
      f'{medida / 1000}km.')