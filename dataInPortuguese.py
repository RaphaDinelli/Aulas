# This program print a date in portuguese(Brazil) format.

from time import asctime

print(asctime())

x = asctime()

data = {'Sun': 'Domingo', 'Mon': 'Segunda-Feira', 'Tue': 'Terça-Feira', 'Wed': 'Quarta-Feira', 'Thu': 'Quinta-Feira', 'Fri': 'Sexta-Feira', 
'Sat': 'Sabado', 'Jan': 'Janeiro', 'Feb':'Fevereiro', 'Mar': 'Março', 'Apr': 'Abril', 'May': 'Maio', 'Jun':'Junho', 'Jul': 'Julho',
'Aug': 'Agosto', 'Set': 'Setembro', 'Oct':'Outubro', 'Nov': 'Novembro', 'Dec': 'Dezembro'}

print(data[x[0:3]], x[8:10])

print('%s, %s de %s de %s' %(data[x[0:3]], x[8:10], data[x[4:7]], x[-4:]))
