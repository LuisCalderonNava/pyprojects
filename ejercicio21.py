print("---------------------------------------------------------------------------------------------------------")
print("Algoritmo que indica si un triángulo es equilátero, isósceles o escaleno dadas las longitudes de sus lados")
#Algoritmo que indica si un triángulo es equilátero, isósceles o escaleno dadas las longitudes de sus lados
a = 4
b = 4
c = 4
print("El primer lado del triangulo mide: " ,a)
print("El segundo lado del triangulo mide: " ,b)
print("El tercer lado del triangulo mide: " , c)

if(a == b and a == c):
    print("Es un triangulo EQUILATERO")
elif (a == b or a == c or b == c):
    print("Es un triangulo ISOSCELES")
else:
    print("Es un triangulo ESCALENO")
print("---------------------------------------------------------------------------------------------------")