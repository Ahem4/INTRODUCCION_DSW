x =float(input("ingrese la velocidad del automovil en km/h: "))
if  x <=30:
     print("pertenece a zonas escolares")
     print("no infringe el limite de velocidad")
elif x <=60:
    print("`pertenece a vias urbanas")
    print("supera el limite de zonas escolares")
elif x <=80:
    print("pertenece a vias rurales")
    print("supera los limites de zonas escolares y vias urbanas")
elif x <=100:
    print("pertenece a rutas nacionales")
    print("supera los limites de zonas escolares, urbanas y rurales")
else:
    print("supera todos los limites de velocidad establecidos")
