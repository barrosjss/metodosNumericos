# Team @Barros @DeLaPeña
# Curso : Metodos Numericos

"""
DESCRIPCION: Determinar el equivalente decimal de un numero binario almacenado en el 
formato de punto flotante y viceversa, el equivalente binario almacenado en el formato
de punto flotante de un numero decimal.
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
    
#-------------conversion binario parte entera y parte decimal----------------

def binario(numCon):
    '''
    
    se recibe el numero a convertir a binario en modo flotante 
    ----------
    numCon : flotante
        DESCRIPTION.
        numCon contendra el numero a convertir que sera separado en su 
        version entera y en al decimal
    Returns
    -------
    res : TYPE: string
        DESCRIPTION.
        se ira agregando al final de la cadena el resultado que se genere en
        la operacion
    cad1 : TYPE: string
        DESCRIPTION.
        contendra los bits de la parte entera
    cad2 : TYPE: string
        DESCRIPTION.
        contendra los bits de la parte decimal para utilizarlo mas adelante
    '''
        
    entera, dec = str(numCon).split(".")      
    dec, entera = math.modf(numCon)
    entera = int(entera) 
    
    res = format(entera, 'b') + '.'
    aux = format(entera, 'b') 
    cad1 = aux
   
    cad2 = str()
    
    for i in range(6):        
        
        dec = dec*2

        if int(dec) == 1 or int(dec) ==0:
            entera = str(int(dec))
            res += entera
            dec,ent = math.modf(dec)
            
            cad2 +=  entera
    print(type(res))
    return res, cad1, cad2

#-----------------------notacion cientifica binario--------------------------

def Notacion(entero, decimal):
    
    aux = entero[0]
    aux1 = entero[1:len(entero)]
    expo = len(aux1)
    NotaCi = aux + '.'+aux1 +decimal
    
    cient = str(2 ) +'^'+ str(len(aux1) )
    
    bits = aux1+decimal
    
    return NotaCi, cient, expo,bits

#----------------------------estandar IEEE745--------------------------------

def estandar(exponencial,numero, signo = str(1) ):
    
    bits = str(format(127+exponencial,'b'))
    
    ceros = 23 - len(numero)
    
    for i in range(ceros):
        numero += str(0)

    return signo,bits,numero

#-------------------------regreso al numeor original------------------------

def numregreso():
    
    regreso = input('quieres regresar el numero (si / no): ')
    if regreso == 'si' or regreso =='SI':
           sigre = input('ingresa el signo: ')
           bits8re = input('ingrese los bits: ')
           numere = input('ingrese el numero en bits: ')
           
           if sigre == '0':
               
               print('Estandar IEEE754: [',sigre,'] [',bits8re,'] [',numere,']')
               
               bina , notacion,expon = returnCientifica(bits8re,numere)
               print('binario notacion cientifica: ', bina, '---> ',notacion)
               
               binario, flotante = decimalreturn(expon, bina)
               print('numero punto flotante binario: ', binario)
               print('Tu numeor es: ', flotante)
           else:
               
               print('Estandar IEEE754: [',sigre,'] [',bits8re,'] [',numere,']')
               
               bina , notacion,expon = returnCientifica(bits8re,numere)
               print('binario notacion cientifica: -', bina, '---> ',notacion)
               
               binario, flotante = decimalreturn(expon, bina)
               print('numero punto flotante binario: -', binario)
               print('Tu numeor es: -', flotante)
               
                
            
               
           
           
    elif regreso == 'no' or regreso =='NO':
            pass
    elif regreso != 'si' or regreso != 'SI' or regreso != 'no' or regreso != 'NO':
        numregreso()

#-------------------------regreso a numero decimal------------------------

def decimalreturn(exponente, cadbi  ):
    
    exponente = exponente+2
    a = cadbi[0]+cadbi[2:exponente]+'.'+cadbi[exponente:len(cadbi)]
    punto = a.index('.')
    entero = a[0:punto]
    entero = int(entero,2)
    
    decimal = a[punto+1:len(a)]
    dec =returndecimal(decimal)
    
    flotante = int(entero)+float(dec)
    return a, flotante


#-----------------------regreso a notacion cientifica------------------------

def returnCientifica(bits8, numerobi):
    
    bit8 = int(bits8,2)
    exponente = bit8-127
    
    numerobi = '1' +'.'+ numerobi
    cient = str(2 ) +'^'+ str(exponente )
    
    return numerobi, cient,exponente
    
#-----------------------numero flotante ------------------------

def decimal(cadbi  ):
    
    punto = cadbi.index('.')

    ente = cadbi[0:punto]
    decimal = cadbi[punto+1:len(cadbi)]

    ente = int(ente,2)
        
    dec = returndecimal(decimal)
    
    flotante = int(ente)+float(dec)
    return  flotante    

def returndecimal(decimal):
    dec = 0
    for i in range(len(decimal)):
        if decimal[i] == '1':
            ex = i+1
            dec += pow(2, -ex)
    return dec            
    
    

#-------------------menu de seleccion decimal o binario----------------------  
  
def menu(terminar):
    while terminar == 'si':
        opcion = input("Numero decimal o binario  (d / b): ")    
        
        if opcion == 'd' or opcion == 'D':
            num = float(input('Ingresa tu numero: '))
            
            if num > 0:
                
                cadori, cad1,cad2 = binario(num)
                print('numero punto flotante binario: ', cadori)    
                
                nota, cien ,expo,bits = Notacion(cad1,cad2)
                print('numero binario notacion cientifica: ',nota, '---> ', cien)
                
                sig, bits8 , nume = estandar(expo,bits, str(0))
                print('Estandar IEEE754: [',sig,'] [',bits8,'] [',nume,']')
                
                numregreso()                          
                
            else:
                
                
                num = str(num)
                signo = num[0]
                numero = num[1: len(num)]
                                
                print('signo: [',signo,'] numero: [',numero,']')
                                
                cadoir, cad1,cad2 = binario(float(numero))
                print('numero punto flotante binario: ',signo,cadoir)
                nota, cien ,expo,bits = Notacion(cad1,cad2)
                print('numero binario notacion cientifica: ',nota, '---> ', cien)
                
                sig, bits8 , nume = estandar(expo,bits, str(1))
                print('Estandar IEEE754: [',sig,'] [',bits8,'] [',nume,']')
                
                numregreso()
            
        elif opcion == 'b' or opcion == 'B':
            
            numbi = input('Ingresa tu numero binario flotante: ')
            
            print('numero binario: ',numbi)
            cadori = decimal(numbi)
            print('numero punto flotante: ', cadori)    
            
            cadori, cad1,cad2 = binario(cadori)
                
            
            nota, cien ,expo,bits = Notacion(cad1,cad2)
            print('numero binario notacion cientifica: ',nota, '---> ', cien)
            
            sig, bits8 , nume = estandar(expo,bits, str(0))
            print('Estandar IEEE754: [',sig,'] [',bits8,'] [',nume,']')
            
            numregreso() 
        elif opcion != 'b' or opcion != 'B' or opcion != 'd' or opcion != 'D':
            menu(terminar)
        else:
            print('!!!!!!opcion no ingresada correctamente!!!!!')
            
        inicio()   
            
#---------------------------------inicio-------------------------------------
inicio()