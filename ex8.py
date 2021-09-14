#Faça um programa que pergunte em que turno você estuda. 
#Peça para digitar “M” para matutino, “V” para vespertino ou “N” para noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.



def exercicio_08(mensagem):
    print("Digite a letra correspondente ao seu turno:")
    print("M para turno matutino")
    print("V para turno vespertino")
    print("N para turno noturno")
    print("X para sair.")
    letra = input(mensagem)
    
    if letra == "M":
        print("Bom Dia!")
    elif letra == "V":
        print("Boa Tarde")
    elif letra == "N":
        print("Boa Noite")
    elif letra == "X":
        print("No class!")
    else:
        print("Valor Inválido")

    
    
print(exercicio_08("Informe uma letra: "))
