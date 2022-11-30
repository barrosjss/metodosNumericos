# FUNCIONES
# --------------------------------------------
# Funcion para Convertir el numero decimal a binario
def decimalBinario(decimal):
    bina = " "
    bin(int(decimal))
    binario = int(bin(decimal)[2:])
    return binario

# Funcion para Convertir la parte decimal de un numero binario a decimal


def parteDecimalABinario(decimal):
    binD = ""
    decimal = float("0." + str(decimal))
    for i in range(10):
        decimal = decimal * 2
        if (str(decimal)[0] == "0"):
            binD = binD + "0"
        elif (str(decimal)[0] == "1"):
            decimal = decimal - 1
            binD = binD + "1"
    return binD

# -------------------------------------------
# Toma un numero decimal y separa la parte entera


def parteEntera(numero):
    numeroStr = str(numero)
    entero = ""
    puntoPos = len(numeroStr)
    for i in range(len(numeroStr)):
        if (numeroStr[i] != "."):
            entero = entero + numeroStr[i]
        elif (numeroStr[i] == "."):
            puntoPos = i
            break
    return int(entero), puntoPos

# Toma un numero decimal y separa la parte decimal


def parteDecimal(numero, puntoPos):
    numero = str(numero)
    decimal = ""
    for i in range(len(numero)):
        if (i > puntoPos):
            decimal = decimal + numero[i]
    intDecimal = int(decimal)
    return intDecimal

# Toma un numero decimal y separa la parte entera y decimal


def separarNumero(numero):
    entero, puntoPos = parteEntera(numero)
    decimal = 0
    if puntoPos != len(str(numero)):
        decimal = parteDecimal(numero, puntoPos)
    return entero, decimal


def extraerSigno(numero):
    numero = str(numero)
    signo = "0"
    if numero[0] == "-":
        signo = "1"
        numero = numero[1:len(numero)]
    return signo, float(numero)


def calcularExp(entero, decimal, bitsExp, numero):
    expmax = 2**bitsExp
    e = 0
    entero = str(entero)
    #numero = ""

    if (abs(numero) > 1):
        e = len(entero) - 1

    else:
        if (numero < 1):
            e -= 1
            while decimal[0] == 0:
                decimal = decimal[1:len(decimal)]

    print("e" + str(e))

    exp = e + (expmax // 2)
    print("exp: " + str(exp))
    return exp

##############################################


numero = float(input("Ingrese el numero decimal: "))
#bitsNumero = int(input("Ingrese el numero de bits del número: "))
#bitsMantisa = int(input("Ingrese el número de bits de la mantisa: "))
#bitsExp = bitsNumero - bitsMantisa - 1

signo, numero = extraerSigno(numero)
entero, decimal = separarNumero(numero)
print(str(decimalBinario(entero)) + "." + str(decimalBinario(decimal)))

#exp = decimalBinario(calcularExp(entero, decimal, bitsExp, numero))

#mantisa = str(decimalBinario(entero)) + str(decimalBinario(decimal))
#numero_binario = str(signo) + " " + str(exp) + " " + mantisa
#print("El número en binario punto flotante es: " + numero_binario)
