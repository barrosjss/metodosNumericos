import math

#Funciones
def funcion(x): #Calcular f(x)
    x = math.radians(x)
    #resultado = math.log(x) #Define la funcion f(x)
    resultado = math.e**(2*x)
    return resultado
 
#Primera derivada

##Diferencias finitas progresivas

###Dos puntos
def pd_dfp_2p(x,h):
    fpx = (funcion(x + h) - funcion(x))/h
    print('La primera derivada por el método de diferencias progresivas de dos puntos es: ', fpx)

###Tres puntos
def pd_dfp_3p(x,h):
    fpx = ((-3*funcion(x)) + (4*funcion(x+h)) - (funcion(x+ 2*h)))/(2*h)
    print('La primera derivada por el método de diferencias progresivas de tres puntos es: ', fpx)
    
##Diferencias finitas centradas

###Tres puntos
def pd_dfc_3p(x,h):
    fpx = ((funcion(x+h))-funcion(x-h))/(2*h)
    print('La primera derivada por el método de diferencias centradas de tres puntos es: ', fpx)

###Cuatro puntos
def pd_dfc_4p(x,h):
    fpx = ((funcion(x-2*h))-(8*funcion(x-h))+(8*funcion(x+h))-(funcion(x+2*h)))/(12*h)
    print('La primera derivada por el método de diferencias centradas de cuatro puntos es: ', fpx)

##Diferencias finitas regresivas

###Dos puntos
def pd_dfr_2p(x,h):
    fpx = (funcion(x)-funcion(x-h))/h
    print('La primera derivada por el método de diferencias regresivas de dos puntos es: ', fpx)

###Tres puntos
def pd_dfr_3p(x,h):
    fpx = ((funcion(x-2*h))-(4*funcion(x-h))+(3*funcion(x)))/(2*h)
    print('La primera derivada por el método de diferencias regresivas de tres puntos es: ', fpx)
    
#Segunda derivada

##Diferencias finitas progresivas

###Dos puntos
def sd_dfp_2p(x,h):
    f2px = ((funcion(x))-(2*funcion(x+h))+(funcion(x+2*h)))/h**2
    print('La segunda derivada por el método de diferencias progresivas de dos puntos es: ', f2px)

###Tres puntos
def sd_dfp_3p(x,h):
    f2px = ((2*funcion(x))-(5*funcion(x+h))+(4*funcion(x+2*h))-(funcion(x+3*h)))/h**2
    print('La segunda derivada por el método de diferencias progresivas de tres puntos es: ', f2px)

##Diferencias finitas centradas

###Tres puntos

def sd_dfc_3p(x,h):
    f2px = ((funcion(x-h))-(2*funcion(x))+(funcion(x+h)))/h**2
    print('La segunda derivada por el método de diferencias centradas de tres puntos es: ', f2px)

###Cinco puntos

def sd_dfc_5p(x,h):
    f2px = (-(funcion(x-2*h))+(16*funcion(x-h))-(30*funcion(x))+(16*funcion(x+h))-(funcion(x+2*h)))/(12*h**2)
    print('La segunda derivada por el método de diferencias centradas de cinco puntos es: ', f2px)

##Diferencias finitas regresivas

###Dos puntos

def sd_dfr_2p(x,h):
    f2px = ((funcion(x-2*h))-(2*funcion(x-h))+(funcion(x)))/h**2
    print('La segunda derivada por el método de diferencias regresivas de dos puntos es: ', f2px)

###Tres puntos

def sd_dfr_3p(x,h):
    f2px = (-(funcion(x-3*h))+(4*funcion(x-2*h))-(5*funcion(x-h))+(2*funcion(x)))/h**2
    print('La segunda derivada por el método de diferencias regresivas de tres puntos es: ', f2px)


#################################

x0 = 1.1
h = 0.1

pd_dfp_2p(x0, h)
pd_dfp_3p(x0, h)
pd_dfc_3p(x0, h)
pd_dfc_4p(x0, h)
pd_dfr_2p(x0, h)
pd_dfr_3p(x0, h)
sd_dfp_2p(x0, h)
sd_dfp_3p(x0, h)
sd_dfc_3p(x0, h)
sd_dfc_5p(x0, h)
sd_dfr_2p(x0, h)
sd_dfr_3p(x0, h)