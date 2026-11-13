try:
    resultado=10/0
    print("Resultado:",resultado)
except ZeroDivisionError:
    print("Error:no se dividir entre cero")

try:
    numero=int(input("ingrese un numero entero: "))
    print("numero ingresado: ",numero)
except ValueError:
    print("Error: Debe ingresar un numero valido")
