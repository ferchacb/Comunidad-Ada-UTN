#Return y parametros
x = int(input("Valor para x: "))
y = int(input("Valor para y: "))
def suma (x,y):
    z= x + y
    return z


#Respuesta 1 del examen, calcular edad
def calcularEdad():
    actual = int(input("Ingrese el año actual: "))
    nombre = str(input("Ingrese un nombre: "))
    naci = int(input("Ingrese el año de nacimiento: "))
    edad = actual - naci
    print("Nombre:",nombre,", año de nacimiento:",naci,", edad:",edad)


#Una función que obtenga el área de un triangulo.
base = float(input("Dígite la base del triángulo:"))
altura = float(input("Dígite la altura del triángulo:"))
def triangu():
    area = (base)*(altura) / 2
    print("El área del triángulo es:",area)

print("La suma entre X con Y es:",suma(x,y))
print("Programa Finalizado")

suma(x,y)
calcularEdad()
triangu()