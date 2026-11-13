votosValidos=int(input("ingrese votos vaslidos: "))
votosPartido=int(input("ingrese votos por su partido: "))

umbral= votosValidos*0.03

if votosPartido > umbral:
    print("tu partido tendra curules")
else:
    print("se quemaron")
