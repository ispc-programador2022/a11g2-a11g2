#Issue nro 8 - Agustin
def modulo(x,y):
    try:
        res=x%y
    except ZeroDivisionError:
        return 'No se puede dividir por cero'    
    else:
        return res
