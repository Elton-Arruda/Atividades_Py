s = float(input('Digite o salário do funcionário: R$ '))
#Utilização do 'R$' para impedir que o programa apresente erros por digitação de usuário.
ns = s+(s*15/100)
print('Com o aumento de 15%, o novo salário do funcionário será R$ {:.2f}'.format(ns))
#Porcentagem básica com {:.2f} para organizar o resultado e ficar de acordo com o padrão já conhecido.
