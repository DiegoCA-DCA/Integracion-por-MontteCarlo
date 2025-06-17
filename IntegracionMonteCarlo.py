import numpy as np
import math
import matplotlib.pyplot as plt

def MonteCarlo1D (f, a, b, N):

    '''
    Integracion Monte Carlo para una funcion f en el intervalo [a,b].

    Argumentos:
        f(funcion):Funcion a integrar.
        a(float): Limite inferior.
        b(float): Limite superior.
        N(int): Numero de puntos aleatorios

    Retorna:
        Float: Aproximacion de la integral
    '''


    #Generar N úntos aleatorios en [a,b]
    x_aleatoria = np.random.uniform(a, b, N)
    #Evaluar la funcion en los puntos aleatorios
    fvalores = f(x_aleatoria)
    #Calcular el promedio y multiplicar por le ancho (b-a)
    integral = (b - a) * np.mean(fvalores)
    return integral

#Ejemplo: Integral de 1/(ln X) en [3,8]
f = lambda x: 1 / np.log(x)
a, b= 3, 8
N = 10000 #Numero de puntos
resultado = MonteCarlo1D(f, a, b, N)
print(f'Aproximacion Monte Carlo (1D): {resultado: .6f}')

#Visulaizacion de datos
x = np.linspace(a, b, 400)
y = f(x)
plt.plot(x,y,'r-', linewidth = 2, label = 'f(x) = x^2')
plt.fill_between(x, y, color = 'orange', alpha = 0.3)
plt.legend()
plt.title('Integracion Monte Carlo 1D')
plt.show()
