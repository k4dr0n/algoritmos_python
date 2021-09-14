#Faça um programa para o cálculo de uma folha de pagamento, 
#sabendo que os descontos são dados na lista abaixo. 
#O Salário Líquido corresponde ao Salário Bruto menos os descontos (imposto e sindicato). 
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês, 
#e deve imprimir todos os cálculos realizados. O desconto do IR é calculado conforme a tabela em seguida.

# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo):
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%

# 3% do salário bruto para o Sindicato;

# O FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).


    
def salario(horas_trabalhadas, valor_hora=10):
  return horas_trabalhadas * valor_hora

def relatorio_salario(horas_trabalhadas, valor_hora):
    salario_bruto = salario(horas_trabalhadas, valor_hora)

    fgts = 0.11 * salario_bruto
    sind = 0.03 * salario_bruto

    salario_liquido = salario_bruto  - sind

    if salario_bruto > 900 and salario_bruto <=  1500:
        irpf = 0.05 * salario_bruto
        salario_liquido = salario_bruto - irpf

    elif salario_bruto > 1500 and salario_bruto <= 2500:
        irpf = 0.10 * salario_bruto
        salario_liquido = salario_bruto - irpf

    else:
        irpf = 0.20* salario_bruto
        salario_liquido = salario_bruto - irpf




    print("Salário por hora trabalhada: R$ %5.2f" % valor_hora)
    print("Número de horas trabalhadas no mês: %4d" % horas_trabalhadas)
    print("------------------------------------------------")
    print("Seu salario bruto e : R$ %7.2f" % salario_bruto)
    print("O valor de seu FGTS e de: R$ %6.2f" % fgts)
    print("O sindicato vai te levar: R$ %5.2f" % sind)
    print("Seu salario liquido e de: R$ %7.2f" % salario_liquido) 
    
    if salario_bruto <= 900: 
        print("Parabéns (ou não), você está isendo de Imposto!")
    else:
        print("Você foi extorquido em: R$ %6.2f de Imposto!" % irpf) 


hora = float(input("Informa o valor recebido por hora trabalhada em R$. "))
n_horas = float(input("Informe a quantidade de horas trabalhadas no mes. "))

relatorio_salario(n_horas, hora)
