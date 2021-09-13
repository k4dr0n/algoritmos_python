ano = int(input('Ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')
    
from calendar import isleap

ano = 2021

if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')
    
    
