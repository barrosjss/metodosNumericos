import math

# este es el numero que queremos convertir a binario
numero = 29

# ------------------------------------------------------------------

# Pasar numero entero a binario

def entero_a_binario(num_entero):
  # Pasar numero entero a binario
  binary = bin(num_entero)
  return binary

# ------------------------------------------------------------------

# Pasar numero decimales a binario

def decimal_a_cualquier_base(decimal, base, digitos):
    # Debemos separar la parte entera y decimal, algo que podemos hacer con modf en Python.
    parte_fraccionaria, parte_entera = math.modf(decimal)

    parte_entera = int(parte_entera)
    cadena_parte_entera = ""
    cadena_parte_fraccionaria = ""

    # Debemos seguir el procedimiento que hacemos manualmente:

    # En el caso de la parte entera vamos dividiéndola entre la base y usando el 
    # residuo para saber cuál digito irá en el resultado.

    while parte_entera > 0:
        residuo = parte_entera % base
        digito = digitos[int(residuo)]
        cadena_parte_entera += digito
        parte_entera = int(parte_entera/base)

    # Invertir cadena de parte entera
    cadena_parte_entera = cadena_parte_entera[::-1]
    sobrante = None

    #Para la parte decimal o fraccionaria, vamos a ir multiplicando el valor decimal por 
    # la base, usar la parte entera del resultado como dígito para el resultado, y asignando 
    # la parte decimal a la parte fraccionaria original.

    while True:
        resultado = parte_fraccionaria*base
        parte_fraccionaria, sobrante = math.modf(resultado)
        digito = digitos[int(sobrante)]
        cadena_parte_fraccionaria += digito
        if sobrante == 0:
            break

    return cadena_parte_entera + "." + cadena_parte_fraccionaria

# ------------------------------------------------------------------

# Seccion de pruebas
en_binario = decimal_a_cualquier_base(numero, 2, "01")
en_octal = decimal_a_cualquier_base(numero, 8, "01234567")
en_hexadecimal = decimal_a_cualquier_base(numero, 16, "0123456789ABCDEF")
print(f"El decimal {numero} es {en_binario} en binario, {en_octal} en octal y {en_hexadecimal} en hexadecimal")

# ------------------------------------------------------------------