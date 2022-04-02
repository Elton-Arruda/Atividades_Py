from math import radians, sin, cos, tan
#Podemos, e fizemos, também importar mais de um item, sem precisarmos importar a biblioteca inteira - deixando o código mais limpo.
angulo=float(input('Digite o ângulo desejado: '))
seno=sin(radians(angulo))
print('O ângulo tem {} tem o SENO de {:.2f}'.format(angulo,seno))
coseno=cos(radians(angulo))
print('O ângulo tem {} tem o COSENO de {:.2f}'.format(angulo,coseno))
tangente=tan(radians(angulo))
print('O ângulo tem {} tem o TANGENTE de {:.2f}'.format(angulo,tangente))
