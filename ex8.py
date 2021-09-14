#!/usr/bin/python

# Faça um programa que pergunte em que turno você estuda. 
# Peça para digitar “M” para matutino, “V” para vespertino ou “N” para noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.



def vogal_consoante(letra):
  # letra = letra.lower()
  # if letra in ["a", "e", "i", "o", "u"]:
  if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(letra, "é vogal")
  else:
    print(letra, "é consoante")

sexo = raw_input("Digite F se for feminino e M se for masculino. ")

if sexo == 'M':
    print("Sexo e Masculino.")
elif sexo == 'F':
    print("Sexo e Feminino. ")
else:
    print("Informacao invalida.")
