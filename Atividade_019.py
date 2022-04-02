from random import choice
aluno1=str(input('Primeiro aluno: '))
aluno2=str(input('Segundo Aluno: '))
aluno3=str(input('Terceiro aluno: '))
aluno4=str(input('Quarto Aluno: '))
lista=[aluno1,aluno2,aluno3,aluno4]
sorteado=choice(lista)
#Pelo fato de se tratar de uma escolha de apenas um aluno, acredito que o choice se encaixa melhor.
print('O sorteado foi {}'.format(sorteado))
#Penso, na verdade, se existiria uma forma de fazer com algum outro da biblioteca random.
