# Team @Barros @Donado @Lerma
# Curso : Metodos Numericos

"""
DESCRIPCION: Ingresar un numero decimal y pasarlo a cualquier base.
"""

import sys
import math

#-------------------comprobacion del 'si' o del 'no'------------------------
def inicio():
    '''
    obtiene el dato de confirmacion si es un 'si' o un ' no'
    en sus dos versiones minusculas y mayusculas
    Returns: vuelve a regresar a preguntar por la confirmacion
    -------
    
    se repitira hasta que se ingrese la confirmacion correcta
    '''    
    terminar = input('ingresar numero (si / no): ')
 
    if terminar == 'si' or terminar == 'SI':
        menu(terminar)
    elif terminar == 'no' or terminar == 'NO':
        print('!!!!! termino del programa !!!!!')
        sys.exit()
    elif terminar != 'si' or terminar != 'SI' or terminar != 'no' or terminar != 'NO':
        print('valor incorrecto')
        inicio()
        
#------------------------decimal a alguna base-----------------------------

def any_base(decimal, base, digitos):
    # Debemos separar la parte entera y decimal, algo que podemos hacer con modf en Python.
    parte_fraccionaria, parte_entera = math.modf(decimal)

    parte_entera = int(parte_entera)
    cadena_parte_entera = ""
    cadena_parte_fraccionaria = ""

    # Debemos seguir el procedimiento que hacemos manualmente:

    # En el caso de la parte entera vamos dividiendola entre la base y usando el 
    # residuo para saber cual digito ira en el resultado.

    while parte_entera > 0:
        residuo = parte_entera % base
        digito = digitos[int(residuo)]
        cadena_parte_entera += digito
        parte_entera = int(parte_entera/base)

    # Invertir cadena de parte entera
    cadena_parte_entera = cadena_parte_entera[::-1]
    sobrante = None

    #Para la parte decimal o fraccionaria, vamos a ir multiplicando el valor decimal por 
    # la base, usar la parte entera del resultado como digito para el resultado, y asignando 
    # la parte decimal a la parte fraccionaria original.

    while True:
        resultado = parte_fraccionaria*base
        parte_fraccionaria, sobrante = math.modf(resultado)
        digito = digitos[int(sobrante)]
        cadena_parte_fraccionaria += digito
        if sobrante == 0:
            break

    return cadena_parte_entera + "." + cadena_parte_fraccionaria



#----------------------------menu de seleccion-------------------------------
    
def menu(terminar):
    while terminar == 'si':
        nums = float(input("Numero a convertir: "))
        
        print('Seleccione la base a convertir: ')
        print('binario = 1 , octal = 2, hexadecimal = 3')
        bases = input("Base: ")   
        
        if bases == '1':
            print(any_base(nums, 2, "01"))
        elif bases == '2':
            print(any_base(nums, 8, "01234567"))
        elif bases == '3':
            print(any_base(nums, 16, "0123456789ABCDEF"))
        else:
            print('!!!!!!opcion no ingresada correctamente!!!!!') 
        
        inicio()

#---------------------------------inicio-------------------------------------
inicio()
