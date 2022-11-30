import math

#Funciones
def funcion(x): #Calcular f(x)
    #x = math.radians(x)
    resultado = math.log(x) #Define la funcion f(x)
    return resultado

def calcular_h(a,b,n): #Calcular el paso
  h=(b-a)/n
  #print('h:',h)
  return float(h)

#Trapecio
def trapecio(a,b):
  n=1
  h=calcular_h(a,b,n)
  resultado = (h/2)*(funcion(b) + funcion(a))
  print('El resultado por el método de trapecio es: ', resultado)
  
#Simpson 1/3
def simpson1_3(a,b):
  n=2
  h=calcular_h(a,b,n)
  resultado = (h/3)*(funcion(a)+4*funcion(a+h)+funcion(b))
  print('El resultado por el métoso de Simpson 1/3 es: ', resultado)
  
#Simpson 3/8
def simpson3_8(a,b):
  n=3
  h=calcular_h(a,b,n)
  resultado = (3*h/8)*(funcion(a) + 3*funcion(a+h) + 3*funcion(a+2*h) + funcion(b))
  print('El resultado por el método de Simpson 3/8 es: ', resultado)
  
#Trapecio compuesto
def trapecio_compuesto(a,b,n):
  h=calcular_h(a,b,n)
  resultado = 0
  for i in range(n):
    x = (h/2)*(funcion(a+h) + funcion(a))
    resultado += x
    a = a + h
    
  print('El resultado por método de Trapecio compuesto es: ', resultado)
  
#Simpson 1/3 compuesto
def c_simpson1_3(a,b,n):
  if (n%2==0):
    h=calcular_h(a,b,n)
    resultado = 0

    sumatoria1 = sum_fxi_impar(a,b,h,n)
    print(sumatoria1)
    sumatoria2 = sum_fxi_par(a,b,h,n)
    print(sumatoria2)
    resultado = (h/3)*(funcion(a) + 4*sumatoria1 + 2*sumatoria2 + funcion(b))
    
    print('El resultado por el método de Simpson 1/3 compuesto es: ', resultado)
    
  else:
    print('Simpson 1/3 compuesto solo se puede utilizar con n par')
    
#Simpson 3/8 compuesto
def c_simpson3_8(a,b,n):
  pass

def sum_fxi_impar(a,b,h,n): #Sumatoria de xi impares
    sum = 0
    for i in range(1,n):
        xi = a + i * h
        if (i%2!=0):
            sum += funcion(xi)
    return sum

def sum_fxi_par(a,b,h,n): #Sumatoria de xi pares
    sum = 0
    for i in range(1,n):
        xi = a + i * h
        if (i%2==0):
            sum += funcion(xi)
    return sum



############################################################


a=float(input('A:')) #Límite inferior
b=float(input('B:')) #Límite superios

trapecio(a,b)
simpson1_3(a,b)
simpson3_8(a,b)
n=int(input('Ingrese n: ')) #Número de intervalos
trapecio_compuesto(a,b,n)
c_simpson1_3(a,b,n)