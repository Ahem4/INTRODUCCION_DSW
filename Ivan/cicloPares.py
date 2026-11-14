n = int(input("ingrese un numero: "))

contador=0
for i in range(0, n+1,2):
    print(i, end=" ")
    contador+=1
    
    if contador ==10:
        print()
        contador=0
if contador !=0:
    print()
