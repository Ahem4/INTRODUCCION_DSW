cantidadFlores= int(input("ingrese la cantidad de flores: "))

if cantidadFlores >=10:
    precioTotal= cantidadFlores*8
    print("total a pagar: "+str(precioTotal))

elif cantidadFlores >=5:
    precioTotal= cantidadFlores*10
    print("total a pagar: "+str(precioTotal))
elif  cantidadFlores ==3:
    print("no debes de pagar nada, las flores son gratis")
else:
    precioTotal= cantidadFlores*15
    print("total a pagar: "+str("precioTotal"))

print("fin programa")
