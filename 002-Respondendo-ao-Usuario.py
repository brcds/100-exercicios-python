#escreva que um programa que receba o nome do usuario e em seguida responda:
#EX:É um prazer te conhecer "José"!

def oi(nome = input('Digite seu nome: ')):
	print(f'É um prazer te conhecer, {nome}')

if __name__ == "__main__":
	oi()