#Función de nombre p2 que debe retornar la suma de los 2 primeros parametros
#  multiplicados por el tercero.

def p2(a,b,c):
    return (a+b)*c

x=float(input('Ingrese el primer valor a sumar: '))
y=float(input('Ingrese el segundo valor a sumar: '))
z=float(input('Ingrese el valor a multiplicar: '))

print('La funcion p2 es: (a+b)*c = ',p2(x,y,z))