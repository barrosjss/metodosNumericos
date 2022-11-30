# pip install numpy
import numpy as np
# pip install matplotlib
import matplotlib.pyplot as plt
# Regla Simpson 1/3


def simpsonUnTercio():
    def fx(x): return np.sqrt(x)*np.sin(x)
    # tramo 1 (a), tramo 2 (b) y tramosTotales
    a = float(input("Ingrese el valor de A: "))
    b = float(input("Ingrese el valor de B: "))
    tramos = int(input("Ingrese el tramo: "))
    print("")
    # Validación de que el tramo sea un número par, y así poder realizar los calculos
    tramoImpar = tramos % 2
    while (tramoImpar == 1):
        tramos = int(input('Ingrese un número par para el tramo: '))
        tramoImpar = tramos % 2
    # Regla de Simpson 1/3, varios tramos
    h = (b - a) / tramos
    xi = a
    # segmento por cada dos tramos
    suma = fx(xi)
    for i in range(0, tramos-2, 2):
        xi = xi + h
        suma = suma + 4*fx(xi)
        xi = xi + h
        suma = suma + 2*fx(xi)
    # último segmento
    xi = xi + h
    suma = suma + 4*fx(xi)
    suma = suma + fx(b)
    area = (h/3)*suma

    # SALIDA
    print('tramos: ', tramos)
    print('Integral: ', area)


menu = int(input("""Digite la opción:
1. "Simpson 1/3
2. Salir """))
print("")
while menu != 2:
    if menu == 1:
        simpsonUnTercio()
    break
