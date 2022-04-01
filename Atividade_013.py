p = float(input('Digite o valor do produto: R$ '))
v = p-(p*10/100)
d = p+(p*10/100)
print('Comprando o produto à vista, você obterá um desconto de 10% e o produto custará R${:.2f}'.format(v))
print('Porém, um taxa de 10% será acrescentada parcelando a compra, sendo assim, o produto custará R${:.2f}'.format(d))
#O código apresenta dois resultados simultâneos: com desconto e com juros; a fim de simplificar o processo e apresentar de uma vez todas as possibilidades.
