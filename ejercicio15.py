import math


print("-------------------------------------------------------------------------------")
print("algoritmo que calcule el área de un triángulo dadas las coordenadas cartesinas de sus vértices")
#algoritmo que calcule el área de un triángulo dadas las coordenadas cartesinas de sus vértices
cx1 = 2 #COORDENADA 
cy1 = 4 #COORDENADA 
cx2 = 1 #COORDENADA 
cy2 = 2 #COORDENADA 
cx3 = 5 #COORDENADA 
cy3 = 6 #COORDENADA 

area = math.abs(cx1 * (cy2 - cy3) + cx2 * (cy3 - cy1) + cx3 * (cy1 - cy2)) / 2

print("coordenada x1 es:" ,cx1)
print("coordenada y1 es:" ,cy1)
print("coordenada x2 es:" ,cx2)
print("coordenada y2 es:" ,cy2)
print("coordenada x3 es:" ,cx3)
print("coordenada y3 es:" ,cy3)
print("el area del triangulo es:" ,area)
print("-------------------------------------------------------------------------------------")