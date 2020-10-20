# faça um programa que leia o nome de 4 alunos e sortei uma sequência para apresentar o trabalho.

from random import shuffle

alunos = []

for c in range(4):
    nome_aluno = input('Digite o nome do aluno: ')
    alunos.append(nome_aluno)

shuffle(alunos)

print(f'A ordem de apresentação será: {alunos}')
