# Funcion de nombre radicación que debe permitir el ingreso de dos parametros y 
# retornar la raiz del primero respecto al segundo

def radicacion(a,b=1):
    try:
        res=round(a**(1/b),3)
    except ZeroDivisionError:
        return 'No se puede dividir por cero'
    else:
        return res


#x=float(input('Ingrese el numero del cual quiere conocer su raiz: ')) ###Debug
#y=float(input('Ingrese el indice de radicacion: '))  ###Debug
#print(radicacion(x,y)) ###Debug
 

