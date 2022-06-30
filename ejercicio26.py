print("--------------------------------------------------------------------------------------------------------------")
print("Algoritmo para saber cuántos dígitos tiene un número entero positivo.")
#Algoritmo para saber cuántos dígitos tiene un número entero positivo.
n = 100988766555
contador = 0

print("E numero que tiene ENTERO es: ",n)
print("")
if(n > 0):
    
    while(n >= 1):
        contador = contador + 1
        n = n /10
    print("El numero tiene un total de: ",contador, " digitos")
    
else:
    print("Su numero NO es positivo")
print("------------------------------------------------------------------------------------------------------------")
    