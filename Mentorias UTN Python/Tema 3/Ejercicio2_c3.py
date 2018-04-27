#Operadores relacionales
def operadores(num1,num2):
    if num1 == num2:
        print("Los numeros son iguales")
    elif num1 != num2:
        print("Los numeros no son iguales")
        if num1 < num2:
            print("Num1 es menor que num2")
        elif num1 > num2:
            print("Num1 es mayor que num2")
        elif num1 <= num2:
            print("Num1 es menor o igual a num2")
        elif num1 >= num2:
            print("Num1 es mayor o igual a num2")
    else:
        ("Error en la entrada de datos")

operadores(19,23)