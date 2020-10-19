#   um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# faça um programa que ajude ele. Lendo o nome deles e escrevendo o nome do escolhido

import random

alunos = []
for c in range(4):
    nome_aluno = input('Digite o nome do aluno: ')
    alunos.append(nome_aluno)

sorteado = random.choice(list(alunos))
print(f'O Sorteado para apagar o quadro foi: {sorteado}')
