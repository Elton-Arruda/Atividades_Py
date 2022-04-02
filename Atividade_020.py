from random import shuffle
aluno1=str(input('Primeiro aluno: '))
aluno2=str(input('Segundo Aluno: '))
aluno3=str(input('Terceiro aluno: '))
aluno4=str(input('Quarto Aluno: '))
#Esse, apesar de parecido com o ex019, sorteira todos os envolvidos de forma aleatória; não apenas um.
lista=[aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
