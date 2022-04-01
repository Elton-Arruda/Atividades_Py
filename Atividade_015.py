d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km você andou com o carro? '))
total = (d*60)+(km*0.15)
#Para economizar linhas, o cálculo foi inteiramente feito se utilizando do parênteses - também preservando a ordem de prioridade da resolução.
print('Com base nos dias e quilometragem, o aluguel custará R${:.2f}'.format(total))
#Código para o cálculo de aluguel de carros - considerando que o dia custa R$ 60,00 e R$0,15 por KM rodados.
