
#Importamos la librera math para usar el metodo sqrt
import math

#Pedimos la entrade de los tres valores de la ecuacio, a = cociente del termino cuadratico, b = cociente de termino lineal y c = termino independiente
a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))
c = float(input("Ingrese el valor de C: "))

#Como nos dice la formula, restamos el valor de b elevado a la 2, con el valode de 4 * a * c
x = (b**2)-(4*a*c)

#Si x es menor que 0, no tendra una solucion dentro de las reglas de los numeros reales
if x < 0:
    print("Solucion solo en numeros complejos")
elif x == 0:
    x1 = (-b) / (2*a)
    print("%.2f" % x1)
else:
	#Luego sumamos o restamos (nos dara 2 valores diferentes, pero ambos igualaran la ecuacion)
	#sumamos el valor de -b a la raiz cuadrada de x y luego lo dividimos entre 2 * a
    x1 = (-b + math.sqrt(x)) / (2*a)
    x2 = (-b - math.sqrt(x)) / (2*a)

    #Mostramos ambos valores
    print("X1: ", x1)
    print("X2: ", x2)



a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c

print("\n**************************\n")

if a == 0:
    print("O valor de a, deve ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1: {}, x2: {}".format(x1, x2))
    
  
