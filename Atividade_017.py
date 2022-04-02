from math import hypot
#Existe a possibilidade de fazer este exercício sem o import, porém, o código fica muito longo.
#Mais uma vez, importamos da biblioteca apenas o necessário.
cateto_oposto=float(input('Digite o valor do cateto oposto: '))
cateto_adjacente=float(input('Digite o valor do cateto adjacente: '))
hipotenusa=hypot(cateto_oposto, cateto_adjacente)
#A partir deste exercício, comecei a deixar as variáveis mais claras - a fim de uma melhor consulta e entendimento de outros.
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
