from math import trunc
#Neste caso, não se faz necessário importar toda biblioteca math, mas só o utilizado para a operação.
num=float(input('Digite um número: '))
print('O valor digitado {} e a sua porção inteira é {}'.format(num, trunc(num)))

#Também existe outra possibilidade de se quebrar um número e obter o mesmo resultado, sendo:
#float(input('Digite um número:' ))
#print('O valor digitado {} e a sua porção inteira é {}'.format(num, int(num)))
