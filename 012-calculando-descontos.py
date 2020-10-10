#   faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço. Com 5% de desconto.

preco = float(input('Qual é o preço do produto: '))
print(f'O produto que custava R${preco:.2f}, na promoção com desconto'
      f' de 5% vai custar R${preco - (preco * 5 / 100):.2f}')
