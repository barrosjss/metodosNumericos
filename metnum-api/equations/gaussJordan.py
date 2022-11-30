from numpy import matrix, linalg
import numpy as np

def crear_matriz(n, m):
    matriz = np.zeros((n, m))
    
    print('Ingresa los datos de la matriz')
    
    for i in range(n):
        for j in range(m):
            x = float(input("Ingrese ({},{}): ".format(i,j)))
            matriz[i][j] = x
    
    return matriz

def gauss_jordan(): 
    n = int(input("Ingrese el tamaño de la matriz: "))
    matrizA = crear_matriz(n, n+1)
    solucion = np.zeros(n)
    
    for i in range(n):
        if matrizA[i][i] == 0:
            print('No es posible continuar, division por cero')
            
        for j in range(i+1, n):
            ratio = matrizA[j][i]/matrizA[i][i]
            
            for k in range(n+1):
                matrizA[j][k] = matrizA[j][k] - ratio * matrizA[i][k]
                
    solucion[n-1] = matrizA[n-1][n]/matrizA[n-1][n-1]
    
    for i in range(n-2, -1, -1):
        solucion[i] = matrizA[i][n]
        
        for j in range(i+1, n):
            solucion[i] = solucion[i] - matrizA[i][j] * solucion[j]
            
        solucion[i] = solucion[i] / matrizA[i][i]
    
    return solucion

def GaussJordan():
    solucion=gauss_jordan()        
    print(solucion)