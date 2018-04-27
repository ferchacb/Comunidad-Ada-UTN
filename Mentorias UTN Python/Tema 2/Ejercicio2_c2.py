#Condicionales if-else
def verifcarParImpar ():
    num = int(input("Digite el numero:\n"))
    if (num%2 == 0):
        print("El numero ingresado: ", num, " es par")
    else:
        print("El numero ingresado: ", num, " es impar")

def comparar(a,b):
    if a == b:
        print("Son iguales")
    else:
        print("No son iguales")


verifcarParImpar()
comparar(5,5)
