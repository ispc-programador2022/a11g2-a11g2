#Aqui se deberá insertar el código. 
import random
from potencia import potencia
from radicacion import radicacion
from producto import producto

#titulo
print("arrancando el codigo del grupo a11g2")

#Issue nro 11 - Ignacio
def p1(parametro1,parametro2,parametro3):
    return suma(producto(parametro1,parametro2),parametro3)
    

#Issue nro 10 - Lourdes
def p2(a,b,c):
    return suma(a,b)*c

#Issue nro 13 - Agustin
def p3(x,y,c):
    res=resta(x,y)
    res=producto(res,c)
    return res

#Issue nro 14 - Agustin
def genrnd():
    lista=[]
    for i in range(50):
        lista.append(random.randint(-256,+256))
    return lista

#Issue nro 15 - Ignacio
def suma_lista(lista):
    acu=0
    for i in range(len(lista)):
        acu+=genrnd[i]
    return acu

#Issue nro 18 - Lina
def calcula_media(lista): 
    res = 0
    for i in range(len(lista)):
    res=suma([res, lista[i]])
    return res

#Issue nro 20 - Lourdes
def calcular_rango():
    list= [min(genrnd()),max(genrnd())]
    return list
    
#Issue nro 21 - Agustin
def calcula_varianza(lista):
    #lista=[1500,1200,1700,1300,1800] --> 228.035
    mean=calcula_media(lista)
    varianza=[]
    sumatoria=0
    for i in lista:
        varianza.append(potencia(resta(i,mean),2))
    for i in varianza:
        sumatoria=suma(sumatoria,i)
    res=cociente(sumatoria,len(lista))
    res=radicacion(res,2)
    return res

#Isue nro 22 - Lourdes
def calcula_min():
    return min(genrnd())

