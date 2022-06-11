#Aqui se deberá insertar el código.
import random

#titulo
print("arrancando el codigo del grupo a11g2")
#Issue nro 6
def producto(parametro1,parametro2):
  return parametro1*parametro2
  

#Issue nro 9
def potencia(numeros):
    return numeros[0]**numeros[1]

  #Issue nro 11
  def p1(parametro1,parametro2,parametro3):
    return suma(producto(parametro1,parametro2),parametro3)
    
#Issue nro 13
def p3(numeros,c):
    res=resta([numeros[0],numeros[1]])
    res=producto([res,c])
    return res

#Issue nro 14
def genrnd():
    lista=[]
    for i in range(50):
        lista.append(random.randint(-256,+256))
    return lista
#Issue nro 15
  def suma_lista(lista):
    acu=0
    for i in range len(lista):
        acu+=genrnd[i]
     return acu

suma_lista(genrnd())

#Issue nro 21
def calcula_varianza(lista):
    #lista=[1500,1200,1700,1300,1800] --> 228.035
    mean=calcula_media(lista)
    varianza=[]
    sumatoria=0
    for i in lista:
        varianza.append(potencia([resta([i,mean]),2]))
    for i in varianza:
        sumatoria=suma([sumatoria,i])
    res=cociente([sumatoria,len(lista)])
    res=radicacion([res,2])
    return res