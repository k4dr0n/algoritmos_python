#Faça um programa que peça um número correspondente a um determinado ano 
#e em seguida informe se este ano é ou não bissexto. 
#Um ano é bissexto se ele é múltiplo de quatro. 
#No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. 
#Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

def check_bissexto(ano):
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        print("Eh Bissexto de acordo com o algoritmo que eu implementei.")
    else:
        print("Não eh bissexto de acordo com o algoritmo que eu implementei.")
    
    
    
ano_inp = int(input('Ano: '))

check_bissexto(ano_inp)
    
from calendar import isleap


if isleap(ano_inp):
    print("Continua bissexto de acordo com o algoritmo do python.")
else:
    print("Continua nao sendo bissexto de acordo com o algoritmo do python.")
