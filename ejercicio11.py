import math


print("....................................................................................")
print("Algoritmo para calcular la distancia entre dos puntos dadas sus coordenadas cartesianas")
#Algoritmo para calcular la distancia entre dos puntos dadas sus coordenadas cartesianas
ax1 = 2
ay1 = 1
bx2 = -3
by2 = 2
print("x1: ",ax1)
print("y1: ", ay1)
print("x2: ", bx2)
print("y2: ", by2)
print("")
resultado = math.sqrt(math.pow(ax1-  ay1, 2) + math.pow(bx2 -  by2, 2))
print("La distancia entre los dos puntos es: ", resultado)
print("---------------------------------------------------------------------------------------")