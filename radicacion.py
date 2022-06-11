# Funcion de nombre radicación que debe permitir el ingreso de dos parametros y 
# retornar la raiz del primero respecto al segundo

def radicacion(a,b=1):
    return round(a**(1/b),3)

x=float(input('Ingrese el numero del cual quiere conocer su raiz: '))
y=float(input('Ingrese el indice de radicacion: '))

print(radicacion(x,y))

