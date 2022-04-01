m = float(input('Quantos metros você deseja calcular? '))
dm = m*10
cm = m*100
mm = m*1000
dam = m/10
hm = m/100
km = m/1000
print('{} possui {:.0f}dm, {:.0f}cm e {:.0f}mm'.format(m, dm, cm, mm))
print('Além disso, possui {}dam, {}hm e {}km'.format(dam, hm, km))
#Código para rápida conversão de tamanhos.
#Utilização do {:.x} para preservar o alinhamento e facilitar o entendimento do resultado.
