print("----------------------------------------------------------------------------------------------------------")
print("Algoritmo para calcular el total a pagar por una compra. Si la compra es de más de $100, el descuento es de 10%, caso contrario no hay descuento")
#Algoritmo para calcular el total a pagar por una compra. Si la compra es de más de $100, el descuento es de 10%, caso contrario no hay descuento
compra = 155
print("El total a pagar: ",compra)
print("______________________")
if(compra > 100):
    print("SE GANO UN DESCUENTO DE 10% POR TENER MAS DE 100 PESOS DE COMPRA")
    r = compra*0.1
    desc = compra-r
    print("tuvo descuento de: ",r)
    print("AHORA SU TOTAL A PAGAR VA A SER ESTO: ",desc)   
else:
    print("USTED NO TIENE DESCUENTO")
print("--------------------------------------------------------------------------------------------------------")
            