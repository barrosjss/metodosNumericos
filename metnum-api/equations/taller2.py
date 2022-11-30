import numpy as np
import math

# ------------------------------------------------------
def mean_relative_error(y_true, y_pred,):
    relative_error = np.average(np.abs(y_true - y_pred) / y_true, axis=0)
    return relative_error
# ------------------------------------------------------
def calculoPI():
    print(
        f"El número redondeado de PI a cuatro cifras es -{round(math.pi, 4)}")
    errorRedondeo = (round(math.pi, 4) - math.pi)
    print(f"El error de redondeo es {errorRedondeo}")
# ------------------------------------------------------
def valoresIngresados():
    num = float(input("Digite un número: "))
    # Método Round, sirve para redondear los números y la cantidad de cifras que desea.
    print(f"El número redondeado a cuatro cifras es - {round(num, 4)}")
    error = (round(num, 4) - num)
    print(f"El error es {error}")
# ------------------------------------------------------
def calculoLogE():
    op = int(input("""Digite la opción: 
    1. Encontrar el logaritmo natural de E.
    2. Encontrar el logaritmo natural de "x" número.
    3. Salir.
    Digite la opción: \n"""))
    while op != 3:
        if (op == 1):
            print(
                f"El logaritmo natural de E, redondeado a 4 cifras es - {round(math.log(math.e, 4))}")
            errorLogE = (round(math.log(math.e, 4)) - math.e)
            print(f"El error de logaritmo natural es - ({errorLogE})")
            break
        elif (op == 2):
            numLog = float(input("Digite un numero: "))
            print(
                f"El número redondeado a cuatro cifras es - {round(numLog, 4)}")
            errorLog = (round(numLog, 4) - numLog)
            print(f"El error del logaritmo ingresado es - {errorLog}")
            break
        elif (menu == 3):
            print("Fin del programa")
            break
# ------------------------------------------------------
def calculoRaizDos():
    op = int(input("""Digite la opción:
    1. Calculo de raíz cuadrada.
    2. Calculo de raíz con "n" número.
    3. Salir.
    Digite la opción: \n """))
    while op != 3:
        if (op == 1):
            resultadoUno = math.sqrt(2)
            print(
                f"El número redondeado a cuatro cifras es - {round(resultadoUno, 4)}")
            errorUno = (round(resultadoUno, 4) - resultadoUno)
            print(f"El error de raíz cubica es - ({errorUno})")
            break
        elif (op == 2):
            base = float(input("Digite la base: "))
            expo = float(input("Digite el exponente: "))
            resultado = math.pow(base, expo)
            print(
                f"La raíz cubica, redondeada a 4 cifras es - {round(resultado, 4)}")
            errorRaizDos = (round(resultado, 4) - resultado)
            print(f"El error de raíz de dos es - ({round(errorRaizDos)})")
            break
        elif (menu == 3):
            print("Fin del programa.")
            break
# ------------------------------------------------------
def calculoRaizTres():
    op = int(input("""Digite la opción:
    1. Calculo de raíz cubica.
    2. Calculo de raíz con "n" número.
    3. Salir.
    Digite la opción: \n """))
    while op != 3:
        if (op == 1):
            resultadoUno = np.cbrt(7)
            print(
                f"El número redondeado a cuatro cifras es - {round(resultadoUno, 4)}")
            errorUno = (round(resultadoUno, 4) - resultadoUno)
            print(f"El error de raíz cubica es - ({errorUno})")
            break
        elif (op == 2):
            base = float(input("Digite la base: "))
            expo = float(input("Digite el exponente: "))
            resultado = math.pow(base, expo)
            print(
                f"La raíz cubica, redondeada a 4 cifras es - {round(resultado, 4)}")
            errorRaizDos = (round(resultado, 4) - resultado)
            print(f"El error de raíz de dos es - ({round(errorRaizDos)})")
            break
        elif (menu == 3):
            print("Fin del programa.")
            break
# ------------------------------------------------------
menu = int(input("""Digite la opcion: 
1. Error de redondeo ingresando valores por consola.
2. Error de redondeo de e (base natural del logaritmo).
3. Error de redondeo de constante PI.
4. Error de redondeo de √2
5. Error de redondeo de raiz cubica √7
6. Salir 
Digite la opcion: \n"""))
while menu != 6:
    if (menu == 1):
        valoresIngresados()
        break
    elif (menu == 2):
        calculoLogE()
        break
    elif (menu == 3):
        calculoPI()
        break
    elif (menu == 4):
        calculoRaizDos()
    elif (menu == 5):
        calculoRaizTres()
        break
    elif (menu == 6):
        print("Fin del programa.")
        break
