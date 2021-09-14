#mais facil
#Faça um Programa que peça os 3 lados de um triângulo. 
#O programa deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 

#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes.


# Checar a validade dos dados de entrada
def triangulo_valido(a,b,c):
    if a>0 and b>0 and c>0:
        if a+b>=c and b+c>=a and c+a>=b:
            return True
        else:
            return False
    else:
        return False
    
# Classificador de triângulos
def tipo_triangulo(a,b,c):
    if a==b and b==c:
        print("O triangulo e equilatero.")
    elif a==b or b==c or a==c:
        print("O triangulo e isosceles.")
    else:
        print("O triangulo e escaleno.")

# Leitura dos lados do triangulo
lado_a = float(input("Primeiro lado: "))
lado_b = float(input("Segundo  lado: "))
lado_c = float(input("Terceiro lado: "))

# Teste de validade do triangulo e classificador
if triangulo_valido(lado_a, lado_b, lado_c):
    tipo_triangulo(lado_a, lado_b, lado_c)
else:
    print("O Triangulo nao e possivel para os valores de entrada.")
    print("Dica: Tres lados formam um triângulo quando  a soma de quaisquer dois lados for maior que o terceiro.")




