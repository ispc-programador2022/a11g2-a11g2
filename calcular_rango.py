#Funcion de nombre calcula_rango que debe retornar el rango del array 
# obtenido de la función genrnd
#genrnd: genera un array de 50 numeros aleatorios

import a11g2

def calcular_rango():
    list= [min(a11g2.genrnd()),max(a11g2.genrnd())]
    return list
    
print('El rango de la funcion genrnd() es: ',calcular_rango())


