#Faça um programa que calcule as raízes de uma equação do segundo grau, 
# na forma ax2+bx+c, cuja solução é x=−b±Δ−−√2⋅a, com Δ=b2−4⋅a⋅c. 
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau 
#e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raízes reais, informe-as ao usuário.


import math  #para utilizar a função sqrt

# Checar a validade dos dados de entrada
def check_grau(a):
    if a==0:
        return False
    else:
        return True

def raizes(a,b,c):    
    delta = (b*b)-(4*a*c)
    if delta < 0:
        print("Delta negativo. Equacao nao possui raizes reais!")
    elif delta == 0:
        raiz = -b / (2*a)
        print("Delta = 0. Equacao possui uma raiz real igual a %.2f" % raiz)
    else:
        delta_2 = math.sqrt(delta)
        raiz_1 = (-b + delta_2) / (2*a)
        raiz_2 = (-b - delta_2) / (2*a)
        print("Delta > 0. Equacao possui duas raizes reais." )
        print("Raiz 1 igual a %.2f" % raiz_1)
        print("Raiz 2 igual a %.2f" % raiz_2)
        


#Dados de entrada
print("Considerando ax^2 + bx + c = 0, entre com os seguintes coeficientes")
coef_a = float(input("Valor numerico de a: "))
if check_grau(coef_a):
    print("Equacao de 2o grau. Entre com os demais valores.")
    coef_b = float(input("Valor numerico de b: "))
    coef_c = float(input("Valor numerico de c: "))
    raizes(coef_a,coef_b,coef_c)
else:
    print("Valor de a não pode ser igual a zero!")


        
