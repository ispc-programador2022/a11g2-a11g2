#Aqui se deberá insertar el código. 
import random
from suma import suma
from resta import resta
from producto import producto
from cociente import cociente
from modulo import modulo
from potencia import potencia
from radicacion import radicacion
from datetime import datetime 

#titulo
print("arrancando el codigo del grupo a11g2")

if __name__=='__main__':
    _inicio=datetime.today()

#Issue nro 2 - Natalia
def ing2i(): 
    nro1= int(input("ingrese el primer numero: "))
    nro2= int(input("ingrese el segundo numero: "))
    return (nro1, nro2)

#Issue nro 3 - Agustin
def ing2s():
    x=input('ingrese el primer string: ')
    y=input('ingrese el segundo string: ')
    return x,y

#Issue nro 11 - Ignacio
def p1(parametro1,parametro2,parametro3):
    return suma(producto(parametro1,parametro2),parametro3)
    
#Issue nro 12 - Lourdes
def p2(a,b,c):
    return(producto(suma(a,b),c))

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
        acu+=lista[i]
    return acu

#Issue nro 16 - Natalia
def  producto_lista(lista):
    res =[]
    for _ in lista:
        x=random.choice(lista)
        y=random.choice(lista)
        res.append(producto(x,y))
    return res

#Issue numero 17-Cociente Lista - Horacio   
def cociente_lista(lista):
    res=[]
    while len(res) < 50:
    #for _ in lista:
        x=random.choice(lista)
        y=random.choice(lista)
        aux=cociente(x,y)
        if type(aux)==str:
            continue
        res.append(cociente(x,y))
    return res

#Issue nro 18 - Lina
def calcula_media(lista):
    res=cociente(suma_lista(lista),len(lista))
    return res

#Issue nro 19 - Agustin
def calcula_mediana(lista):
    res=cociente(suma_lista(lista),2)
    return res

#Issue nro 20 - Lourdes
def calcula_rango(lista):
    res=[min(lista),max(lista)]
    return res
    
#Issue nro 21 - Agustin
def calcula_varianza(lista):
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
    #lista=[1500,1200,1700,1300,1800] --> 228.035

#Isue nro 22 - Lourdes
def calcula_min(lista):
    return min(lista)

#Issue nro 23 - Agustin
def calcula_max(lista):
    return(max(lista))

#Issue nro 24 - Agustin
def genrnd5e():
    lista=[]      
    #for i in range(500000000000000000): #no se usa por desbordamiento de memoria
    for i in range(5000000): #Para pruebas 5.000,000 numeros
        lista.append(random.randint(-256,+256))
    return lista

#Issue nro 25 - Agustin
def tiempo_ejecucion():
    #Primer bloque --utilizando genrnd
    comienzo = datetime.today()
    lista = genrnd()
    calcula_mediana(lista)
    calcula_rango(lista)
    calcula_varianza(lista)
    calcula_min(lista)
    calcula_max(lista)
    fin = datetime.today()
    primer_bloque = fin-comienzo
    #Segundo bloque --utilizando genrnd5e
    comienzo=datetime.today()
    lista=genrnd5e()
    calcula_mediana(lista)
    calcula_rango(lista)
    calcula_varianza(lista)
    calcula_min(lista)
    calcula_max(lista)
    fin = datetime.today()
    segundo_bloque = fin-comienzo
    print(f"Primer bloque: {primer_bloque} \nSegundo bloque: {segundo_bloque} \nDiferencia: {segundo_bloque-primer_bloque}")

if __name__=='__main__':
    _tiempo = datetime.today()-_inicio
    print(f'tiempo de ejecucion:{_tiempo}')
     
