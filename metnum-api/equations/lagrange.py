# Código para taller de Interpolación de Lagrade con representación gráfica de puntos
# numpy para hacer los calculos
from multiprocessing import resource_tracker
from turtle import Terminator
import numpy as np

# Para desarrollar los calculos algebraicos de los polinomios
# Para instalar sympy copiamos --> pip install sympy
import sympy as sym
# Para realizar la grafica de los datos
# Para instalar matplotlib copiamos --> pip install matplotlib
import matplotlib.pyplot as plt
# -------------------------------------------------------------------------
# Ingreso de los datos a evaluar Xi y Fi
xi = np.array([0, 0.2, 0.3, 0.4, 0.5])
fi = np.array([1, 1.6, 1.7, 2.0, 2.8])
# -------------------------------------------------------------------------
# Número de elemntos que tendra Xi y Fi
n = len(xi)
x = sym.Symbol("x")
# -------------------------------------------------------------------------
# I = 0,1....., n-1
i = 0
polinomio = 0
# Numerador hara el recorrido de todos los puntos en el vector Xi
# Se hacen dos bucles, i - j, la i validara los valores de Xi y ciclo J los valores de Fi
for i in range(0, n, 1):
    numerador = 1
    denominador = 1
    for j in range(0, n, 1):
        # Si i != j va hacer los calculos para el numerador y denominador de la formula de Lagrange
        if (i != j):
            # (x-xi[j])
            numerador = numerador * (x - xi[j])
            # (xi[i]-xi[j])
            denominador = denominador * (xi[i] - xi[j])
        resultado = (numerador / denominador) * fi[i]
    polinomio = polinomio + resultado
polinomio_simple = sym.expand(polinomio)
print("polinomio")
print(polinomio)
print("Polinomio simple")
print(polinomio_simple)
# ------------------------------------ Representación gráfica ------------------------------------
# convertimos el polinomio de manera simple, tomando como referencia la variable x e indicando la conversion
px = sym.lambdify(x, polinomio)
# muestras es el tramo + 1
muestras = 51
# valor minimo del punto
a = np.min(xi)
# valor maximo del punto
b = np.max(xi)
# Serie de puntos con un intervalo y no se presente distorsion
p_xi = np.linspace(a, b, muestras)
# polinomio de forma de lambda de todos los puntos p_xi
pfi = px(p_xi)
# plt.plot(xi, fi, "o") graficara los puntos que ha calculado y su respectiva marca
plt.plot(xi, fi, "o")
# Creación de puntos de manera lineal
plt.plot(p_xi, pfi)
plt.show()
