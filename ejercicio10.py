
print("------------------------------------------------------------------------------------")
print("algoritmo para calcular el valor total a pagar por dos productos incluyendo el IVA y un impuesto más del 1% (se impone al valor de los productos, antes de calcular el IVA)")
#algoritmo para calcular el valor total a pagar por dos productos incluyendo el IVA y un impuesto más del 1% (se impone al valor de los productos, antes de calcular el IVA)
producto1 = 45
producto2 = 49
print("")
print("Precio del producto 1: ", producto1)
print("Precio del producto 2: ", producto2)

sumaPro = producto1 + producto2
iva = sumaPro*.16
produiva=iva+sumaPro 
print("")
print("Precio a pagar por los productos con el IVA: ",produiva)
impuesto = produiva*0.1
resultadoFinal = impuesto+produiva
print("")# Estos son para hacer espacios entre lineas y que no se vea todo amontonado
print("El total a pagar incluyendo los impuesto seria: ",resultadoFinal)
print("-------------------------------------------------------------------------------------")