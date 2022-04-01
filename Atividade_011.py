n1 = float(input('Qual a largura da sua parede? '))
n2 = float(input('Qual a altura da sua parede? '))
a = (n1*n2)/2
#Mais uma utilização de parênteses para a economia de linhas
print('Você precisará de {}l de tinta para pinta-lá'.format(a))
#Cálculo de Altura*Largura para determinar a quantidade de tinta necessária para pintar uma parede - considerando que 1l pinte 2m²
