n1 = float(input('Quantos reais você tem? R$ '))
d = n1/4.76
e = n1/5.27
#Cotações correspondentes ao dia que o código foi feito - 29/03/2022
print('Você pode converter R${} em US${:.2f} e EUR{:.2f} '.format(n1, d, e))
#Segue o mesmo intuito da conversão de distâncias, porém voltado para moedas estrangeiras - facilmente adaptável a qualquer moeda.
