import math

print("---------------------------------------------------------------------------------------------------------------------")
print("Algoritmo que calcule el área de un triángulo dados los valores de los lados (revise el concepto de semiperímetro)")
#Algoritmo que calcule el área de un triángulo dados los valores de los lados (revise el concepto de semiperímetro)
a = 10
b = 13
c = 7
p = a + b + c
semip = p / 2
area = math.sqrt(semip * (semip - a) * (semip - b) * (semip - c))

print("El valor del lado A: " ,a)
print("El valor del lado B: " ,b)
print("El valor del lado C: " ,c)
print("Area: " ,area)
print("---------------------------------------------------------------------------------------------------------------------")
