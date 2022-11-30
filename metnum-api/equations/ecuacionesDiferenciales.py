import math
import numpy as np
import matplotlib.pyplot as plt

#Funciones
"""
def funcion(t): #Calcular f(x)
t = math.radians(t)
#resultado = math.log(x) #Define la funcion f(x)
resultado = math.e**(2*t)
return resultado
"""

def funcion(y,t):
    e = math.e
    y_prima = 4*(e**(0.8*t)) - 0.5*y
    return y_prima

def siguiente_paso(t0, i, h):
    ti = t0 + i * h
    return ti

def numero_pasos(ti, tf, h):
    n = (tf-ti)/h
    return n    

##Metodo de Euler

def calcular_yimas1(yi, h, phi):
    yimas1 = yi + phi * h
    return yimas1

def metodo_euler(h, ti, tf, yi):
    y = []
    y.append(yi)
    tn = ti
    yn = yi
    for i in range(ti, tf, h):
        phi = funcion(yn, tn)
        yimas1=calcular_yimas1(yn, h, phi)
        y.append(yimas1)
        
        tn = siguiente_paso(ti, i+1, h)
        yn = yimas1
    print(y)
        

##Metodo de Runge-Kutta
def calcular_k1(t, y):
    k1 = funcion(y, t)
    return k1

def calcular_k2(t, y, h, k1):
    k2 = funcion(y+(1/2)*k1*h, t+(1/2)*h)
    return k2
    
def calcular_k3(t, y, h, k2):
    k3 = funcion(y+(1/2)*k2*h, t+(1/2)*h)
    return k3

def calcular_k4(t, y, h, k3):
    k4 = funcion(y+k3*h, t+h)
    return k3

def metodo_rk(h, ti, tf, yi):
    y = []
    y.append(yi)
    tn = ti
    yn = yi
    for i in range(ti, tf, h):
        k1 = calcular_k1(tn, yn)
        k2 = calcular_k2(tn, yn, h, k1)
        k3 = calcular_k3(tn, yn, h, k2)
        k4 = calcular_k4(tn, yn, h, k3)
        yimas1 = yn +(1/6)*(k1+k2+k3+k4)*h
        y.append(yimas1)
        
        tn = siguiente_paso(ti, i+1, h)
        yn = yimas1
    print(y)


###################################

#Valores inicales
h = 1
ti = 0
tf = 4
yi = 2

#Metodo de Euler
metodo_euler(h, ti, tf, yi)

#Metodo de Runge-Kutta
metodo_rk(h, ti, tf, yi)
