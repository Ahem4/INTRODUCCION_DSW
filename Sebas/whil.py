print("1. leche 2. huevos 3. pan 4. azucar 5. sal 6.salir ")
numProd= int(input("Ingrese el numero del producto para consultar el precio: "))
 
while  numProd !=6:
    if numProd==1:
         print("la leche tiene un valor de $9500")
         numProd= 0
    elif numProd ==2:
        print("los huevos tienen un valor de $550")
    elif numProd ==3:
        print("el pam tiene un valor de $3900")
    elif numProd ==4:
        print("el azucar tiene un valor de $5600")
    elif numProd ==5:
        print("la sal tiene un valor de $3400")
    else:
        print("opcion no valida")
    print("-"*20)
    
    print("1. leche 2. huevos 3. pan 4. azucar 5. sal 6.salir ")
    numProd = int(input("ingrese el numero de producto para consultar el precio: "))
    
print("has salido del programa")
