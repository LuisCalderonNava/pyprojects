import math


print("-------------------------------------------------------------------------------------")
print("algoritmo que calcule el valor de la tangente de los lados opuestos a los catetos de un triángulo rectángulo dados los valores de la hipotenusa y uno de los catetos")
#algoritmo que calcule el valor de la tangente de los lados opuestos a los catetos de un triángulo rectángulo dados los valores de la hipotenusa y uno de los catetos
cata = 8
h = 16
catb = h * math.sin(cata)

print("el cateto:" ,cata)
print("la hipotenusa:" ,h)
print("El valor del otro cateto es: " ,catb)
print("----------------------------------------------------------------------------------------")