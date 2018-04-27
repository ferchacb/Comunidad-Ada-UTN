def operacion():
    x = 19
    if x == 10:
        print("x es menor a 10")
    elif x > 0 and x < 10:
        print("x =",x,"esta entre 1 y 10")
    elif x > 10 or x > 20:
        print("x =",x,"es mayor a 10")
    elif x > 10 and x > 20:
        print("No se cumplen ambas condiciones")
    else:
        print("No es ninguna de las opciones")

operacion()
