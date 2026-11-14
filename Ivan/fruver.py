diaSemana = input("Ingrese el dia de la semana: ")
producto = input("Ingrese el producto: ")
valorProducto = float(input("Ingrese el valor del producto: "))

if diaSemana == "lunes" and producto == "fruver":
    valorPagar = valorProducto * 0.7
    print("El descuento es del 30% y el valor a pagar es de:", valorPagar)

elif diaSemana == "martes" and producto == "carnes":
    valorPagar = valorProducto * 0.7
    print("El descuento es del 30% y el valor a pagar es de:", valorPagar)

elif diaSemana == "jueves" and producto == "vinos":
    valorPagar = valorProducto * 0.7
    print("El descuento es del 30% y el valor a pagar es de:", valorPagar)

elif diaSemana == "miercoles":
    if producto == "carnes":
        valorPagar = valorProducto * 0.85
        print("El descuento es del 15% y el costo total es de:", valorPagar)
    elif producto == "fruver":
        valorPagar = valorProducto * 0.9
        print("El descuento es del 10% y el costo total es de:", valorPagar)
    elif producto == "vinos":
        valorPagar = valorProducto * 0.95
        print("El descuento es del 5% y el costo total es de:", valorPagar)

elif diaSemana == "viernes":
    if producto == "vinos":
        valorPagar = valorProducto * 0.85
        print("El descuento es del 15% y el costo total es de:", valorPagar)
    
    elif producto == "fruver":
        valorPagar = valorProducto * 0.9
        print("El descuento es del 10% y el costo total es de:", valorPagar)
    
    elif producto == "carnes":
        valorPagar = valorProducto * 0.95
        print("El descuento es del 5% y el costo total es de:", valorPagar)

else:
    valorPagar = valorProducto
    print("Descuento del 0% y costo total:", valorPagar)
