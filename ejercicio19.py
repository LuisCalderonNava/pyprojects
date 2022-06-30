import math
from this import d


print("------------------------------------------------------------------------------------------------------------------------")
print("algoritmo que calcule las raíces de una ecuación cuadrática cuya forma canónica es ax2+bx+c=0")
#algoritmo que calcule las raíces de una ecuación cuadrática cuya forma canónica es ax2+bx+c=0
a = 5
b = 4
c = 5

print("A: ", a)
print("B: ", b)
print("C: ", c)
if a != 0:
    d = (-b)+(math.sqrt(math.pow(b, 2) + 4*a*c))/2*a
    e = (-b)-(math.sqrt(math.pow(b, 2) + 4*a*c))/2*a
    print("Solucion: " , d ,  " y " ,  e)

else:
    print("El coeficiente no tiene que  ser diferente de cero")
print("------------------------------------------------------------------------------")
