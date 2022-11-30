# Team @Barros @DeLaPeña
# Curso : Metodos Numericos

"""
DESCRIPCION: Crear un código que permita la busqueda de la raiz de una ecuacion no lineal por medio del método de Newton Raphson.
"""

import numpy as np
# Instalar libreria https://es.acervolima.com/como-instalar-numpy-en-macos/

#--------------------------------Ingreso------------------------------------

fx = lambda x: x**3 + 4*(x**2) - 10
dfx = lambda x: 3*(x**2) + 8*x

x0 = 2
tolerancia = 0.001

#-----------------------------Procedimiento---------------------------------

tabla = []
tramo = abs(2*tolerancia)
xi = x0

while(tramo >= tolerancia):
    xnuevo = xi - fx(xi) / dfx(xi)
    tramo = abs(xnuevo - xi)
    tabla.append([xi, xnuevo, tramo])
    xi = xnuevo

#Pasar la lista a un array
tabla = np.array(tabla)
n = len(tabla)

#---------------------------------Salida------------------------------------

print(['xi', 'xnuevo', 'tramo'])
np.set_printoptions(precision=4)
print(tabla)
print('raiz en: ', xi)
print('con error de: ', tramo)