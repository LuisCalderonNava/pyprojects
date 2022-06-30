import math


print("------------------------------------------------------------------------------------------")
print("Algoritmo que calcule el valor de un cateto dados los valores de la hipotenusa y del otro cateto de un triángulo rectángulo")
# Algoritmo que calcule el valor de un cateto dados los valores de la hipotenusa y del otro cateto de un triángulo rectángulo
h = 5
c1 = 3
resultado = math.pow(h, 2) - math.pow(3, 2)
valorCateto = math.sqrt(resultado)
print("valor de la hipotenusa: " ,h)
print("Valor de un cateto: " ,c1)
print("El valor del cateto que falta es: " ,valorCateto)
print("-----------------------------------------------------------------------------")