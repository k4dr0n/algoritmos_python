#!/usr/bin/python
# -*- coding: utf-8 -*-

#Faça um programa para o cálculo de uma folha de pagamento,
#sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para
#o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
#mas não é descontado (é a empresa que deposita).
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
#No exemplo o valor da hora é 5 e a quantidade de hora é 220. 

hora = input("Informa o valor recebido por hora trabalhada. ")
qhora = input("Informe a quantidade de horas trabalhadas no mes. ")

salariob = hora * qhora
fgts = (salariob * 11) / 100
sind = (salariob * 3) / 100

if salariob <= 900:
    salariol = salariob - sind

elif salariob > 900 and salariob <=  1500:
    ir = (salariob * 5) / 100
    salariol = salariob - ir - sind
 
elif salariob > 1500 and salariob <= 2500:
    ir = (salariob * 10) / 100
    salariol = salariob - ir - sind

else:
    ir = (salariob * 20) / 100
    salariol = salariob - ir -sind
    
print("Seu salario bruto e : %7.2f" % salariob)
print("O valor de seu FGTS e de: %7.2f" % fgts)
print("O sindicato vai te levar: %7.2f" % sind)
print("Seu salario liquido e de: %7.2f" % salariol) 




def relatorio_salario(horas_trabalhadas, valor_hora):
  salario_bruto = salario(horas_trabalhadas, valor_hora)

  irpf = 0.11 * salario_bruto
  inss = 0.08 * salario_bruto
  sind = 0.05 * salario_bruto

  salario_liquido = salario_bruto - irpf - inss - sind

  print("Salário por hora trabalhada:", valor_hora)
  print("Número de horas trabalhadas no mês:", horas_trabalhadas)
  print("------------------------------------------------")
  print("Salário bruto:", salario_bruto)
  print("(-) Imposto de Renda:", irpf)
  print("(-) INSS:", inss)
  print("(-) Sindicato:", sind)
  print("(=) Salário Líquido:", salario_liquido)

relatorio_salario(20, 10.5)
