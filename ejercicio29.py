import math


print("-----------------------------------------------------------------------------------------------------------------")
print("Algoritmo para pasar coordenadas polares a cartesianas")
#Algoritmo para pasar coordenadas polares a cartesianas

polar = 5.5;   
o = 240

print("Polar: ", polar)
print("Angulo: ", o)
        
mx = polar * math.cos(o) 
mx2 =  mx * math.cos(60)
my = polar * math.sin(o)
my2 = my *math.sin(60)

print("Coordenadas polares: ",polar)
print("Angulo: " ,o)

print("Ahora la corrdenada X es: " ,mx2)
print("Ahora la coordenada Y es: " ,my2)
print("-----------------------------------------------------------------------------------------------------------------")