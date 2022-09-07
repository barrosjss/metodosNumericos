# Team @Barros @DeLaPeña
# Curso : Metodos Numericos

"""
DESCRIPCION: Crear un código que permita la busqueda de la raiz de una ecuacion no lineal por medio del método de secante.
"""

import math

#--------------------------------Ingreso------------------------------------

f = lambda x: x - math.cos(x)

#-----------------------------Procedimiento---------------------------------

def secante(fun, x_a, x_b, steps = 50):
    
    if fun(x_a) * fun(x_b) >= 0:
        print("El metodo secante no aplica")
        return None
    
    for n in range(steps+1):
        x_n = x_a - fun(x_a) * (x_b - x_a)/(fun(x_b) - fun(x_a))

        if fun(x_n) == 0:
            return x_n
        
        if fun(x_a) * fun(x_n) < 0:
            x_b = x_n
        else:
            x_a = x_n
        
    return x_n

#---------------------------------Salida------------------------------------

print(secante(f, 0, 5, 15))