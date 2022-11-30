from math import *

# Metodo de biseccion
# ------------------------------------------------------
def pol(x):  # Funcion de prueba
    # return x*3 + 4*x2 - 10  # retorna pol(x)=x3+4x*2-10
    return -0.42*x**2 + 2.2*x + 4.7
# ------------------------------------------------------
def trig(x):  # Funcion de prueba
    return x*cos(x-1) - sin(x)  # Retorna tring(x)cos(x-1)-sin(x)
# ------------------------------------------------------
def bisec(f, a, b, tol, n):
    """
    Se implemento el metodo de biseccion
    Las entradas son:
    f = es la funcion
    a = el inicio del intervalo
    b = el fin del intervalo 
    tol = la tolerancia
    n = el numero maximo de iteraciones
    """
    i = 1
    while i <= n:
        p = a + (b-a)/2
        print("i = {0:<2}, p = {1: .12f}".format(i, p))
        if abs(f(p)) <= 1e-15 or (b-a)/2 < tol:
            return p
        i += 1
        if f(a)*f(p) > 0:
            a = p
        else:
            b = p
    """
    Las salidas son:
    p aproximacion a cero de f
    None en caso de que las iteraciones se agoten
    """
    print("Las iteraciones estan agotadas: Error!")
    return None
# ------------------------------------------------------
print("Biseccion funcion pol(x):")
bisec(pol, 1, 2, 1e-8, 100)
"""pol(x), a=1, b=2, tol=10**-8, N_0=100"""
# ------------------------------------------------------
print("Biseccion funcion trig(x):")
bisec(trig, 4, 6, 1e-8, 100)
"""trig(x), a=4, b=6, tol=10**-8, N_0=100"""
