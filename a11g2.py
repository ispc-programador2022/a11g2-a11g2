#Aqui se deberá insertar el código. 
import random
from potencia import potencia
from radicacion import radicacion
from producto import producto
from suma import suma
from cociente import cociente

#titulo
print("arrancando el codigo del grupo a11g2")

<<<<<<< HEAD
#Issue nro 2 - Natalia /// Rehacer
def ing2i():
  return int,int
=======
#Issue nro 2
def ing2i(): 
    nro1= int(input("ingrese el primer numero: "))
    nro2= int(input("ingrese el segundo numero: "))
    return [nro1, nro2]
>>>>>>> 16-producto_lista

#Issue nro 5 - Natalia
def resta(parametro1,parametro2):
    return (parametro1-parametro2)

<<<<<<< HEAD
#Issue nro 11 - Ignacio
def p1(parametro1,parametro2,parametro3):
=======
#Issue nro 6
def producto(parametro1,parametro2):
  return parametro1*parametro2



#Issue nro 9
def potencia(numeros):
    return numeros[0]**numeros[1]

  #Issue nro 11
  def p1(parametro1,parametro2,parametro3):
>>>>>>> 16-producto_lista
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

<<<<<<< HEAD
#Issue nro 16 - Natalia /// rehacer
def  producto_lista():
    return producto(genrnd)
=======
#Issue nro 16
def  producto_lista(lista):
    res =[]
    for _ in lista:
        x=random.choice(lista)
        y=random.choice(lista)
        res.append(producto[x,y])
    return res

producto_lista(genrnd())

>>>>>>> 16-producto_lista

#Issue numero 17-Cociente Lista - Horacio   
import random
def cociente_lista (lista):
    res=[]
    for _ in lista:
        x=random.choice(lista)
        y=random.choice(lista)
        res.append(cociente([x,y]))
    return res

#Issue nro 18 - Lina
def calcula_media(lista): 
    res = 0
    for i in range(len(lista)):
        res=suma([res, lista[i]])   
    return res

#Issue nro 19 - Agustin
def calcula_mediana(lista):
    res=0
    for i in range(len(lista)):
        res=suma([res,lista[i]])
    res=cociente(res,2)
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
def calcula_min(lista):
    return min(lista)

#Issue nro 23 - Agustin
def calcula_max(lista):
    return(max(lista))

#Issue nro 24 - Agustin
def genrnd5e():
    lista=[]      
    for i in range(500000000000000000):
        lista.append(random.randint(-256,+256))
    return lista

