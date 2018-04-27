"""Calcule el total que una persona debe pagar por una llanta.
El precio por unidad es de US$80 000 si se compran menos de cinco y de
US$70 000 si se compran cinco o más llantas."""
def ventaLlantas():
    global unidad
    global precioTotal
    llanta = int(input("Cuantas llantas desea comprar? "))
    if llanta > 0 and llanta < 5:
        unidad = 80000
        precioTotal = (llanta*unidad)
        print("El precio total:",precioTotal)
    elif llanta >= 5:
        unidad = 70000
        precioTotal = (llanta*unidad)
        print("El precio total es:",precioTotal)
    else:
        print("Error en la entrada de datos")
ventaLlantas()