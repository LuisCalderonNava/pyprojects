import math


print("-----------------------------------------------------------------------------")
print("Algoritmo para pasar coordenadas cartesianas a esféricas.")
#Algoritmo para pasar coordenadas cartesianas a esféricas.
a = 3
b = 4
c = 5
print("El punto a es: " ,a)
print("El punto b es: " ,b)
print("El punto c es: " ,c)     


x = math.sqrt(math.pow(a,2) + math.pow(b,2) + math.pow(c,2))
y = math.atan(b/a)
z = math.acos(c/math.sqrt(math.pow(a,2) + math.pow(b,2) + math.pow(c, 2)))

print("El resultado de x es: ",x)
print("El resultado de y es : ",y)
print("El resultado de z es: " ,z)
print("--------------------------------------------------------------------------")
